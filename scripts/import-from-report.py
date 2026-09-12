#!/usr/bin/env -S uv run --quiet --with pyyaml python3
"""Import the learning activities from the working-group report (the source of truth).

Reads `sections/60-design-activities.tex` in the Overleaf clone, converts each
`\\paragraph{\\textbf{LA<NN>. Title}}` block plus its `activitybox` into
`activities/LA<NN>/README.md` (frontmatter + Markdown body), then applies the same
ILO-linking pass as scripts/build-index.py so the two scripts agree.

Usage:  scripts/import-from-report.py [--report ../report] [--only LA05,LA10] [--check]

  --check   regenerate in memory and exit 1 if any activity README differs from the
            report (the import stamp line is ignored when comparing)

Repo-only frontmatter keys are preserved from the existing file and never overwritten:
  expanded_version, status
Everything else (title, keywords, related_ilos, prerequisite_ilos, type, setting,
grouping, mode, duration, assessment, assessed, scale, and the whole body) comes from
the report. Edit the report on Overleaf, pull, and re-run; do not hand-edit the READMEs.

Conversion warnings (stripped \\hl{} notes, unknown LaTeX commands, leftover text after a
box) are printed to stderr so the converter can be extended when the report changes.
"""
import argparse, importlib.util, json, pathlib, re, subprocess, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ACT = ROOT / "activities"
SECTION = "sections/60-design-activities.tex"
PRESERVE = ["expanded_version", "status"]
ID_RE = re.compile(r"\b((?:H|MM|EPR|CS)\d{2}[a-z]?)\b")

spec = importlib.util.spec_from_file_location("build_index", ROOT / "scripts" / "build-index.py")
build_index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_index)

warnings = []
def warn(la, msg):
    warnings.append(f"{la}: {msg}")

# ----------------------------------------------------------------------------- bib

def load_bib(report):
    entries = {}
    for bib in report.glob("*.bib"):
        for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", bib.read_text(), re.S):
            fields = dict(re.findall(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*\n", m.group(3) + "\n", re.S))
            entries[m.group(2)] = {k: v.replace("{", "").replace("}", "").strip() for k, v in fields.items()}
    return entries

def surnames(author):
    names = [a.strip() for a in re.split(r"\s+and\s+", author)]
    def sn(n): return n.split(",")[0].strip() if "," in n else n.split()[-1]
    s = [sn(n) for n in names]
    if len(s) == 1: return s[0]
    if len(s) == 2: return f"{s[0]} and {s[1]}"
    return f"{s[0]} et al."

def cite_inline(e):
    return f"({surnames(e.get('author', '?'))}, {e.get('year', 'n.d.')})"

def cite_full(e):
    url = e.get("url") or (f"https://doi.org/{e['doi']}" if e.get("doi") else "")
    venue = e.get("booktitle") or e.get("journal") or ""
    s = f"{e.get('author', '?')} ({e.get('year', 'n.d.')}). *{e.get('title', '?')}*."
    if venue: s += f" {venue}."
    if url: s += f" <{url}>"
    return s

# ------------------------------------------------------------------- tex → markdown

def strip_comments(tex):
    return re.sub(r"(?<!\\)%.*", "", tex)

def matching(tex, start, open_="{", close="}"):
    """Index just past the brace that closes the one at `start`."""
    depth = 0
    for i in range(start, len(tex)):
        if tex[i] == open_: depth += 1
        elif tex[i] == close:
            depth -= 1
            if depth == 0: return i + 1
    raise ValueError("unbalanced braces")

def split_items(body):
    """Split itemize body on top-level \\item (not inside nested environments)."""
    items, depth, cur, i = [], 0, [], 0
    tokens = re.split(r"(\\begin\{itemize\}|\\end\{itemize\}|\\item\b)", body)
    for t in tokens:
        if t == r"\begin{itemize}": depth += 1; cur.append(t)
        elif t == r"\end{itemize}": depth -= 1; cur.append(t)
        elif t == r"\item" and depth == 0:
            items.append("".join(cur)); cur = []
        else: cur.append(t)
    items.append("".join(cur))
    return [x for x in items if x.strip()]

def itemize_to_md(tex, la, level=0):
    """Replace every top-level itemize environment in `tex` with Markdown bullets."""
    out, pos = [], 0
    while True:
        m = re.search(r"\\begin\{itemize\}", tex[pos:])
        if not m: out.append(tex[pos:]); break
        s = pos + m.start()
        # find matching \end{itemize}
        depth, i = 0, s
        for mm in re.finditer(r"\\begin\{itemize\}|\\end\{itemize\}", tex[s:]):
            depth += 1 if mm.group().startswith(r"\begin") else -1
            if depth == 0: i = s + mm.end(); break
        inner = tex[s + len(r"\begin{itemize}"): i - len(r"\end{itemize}")]
        out.append(tex[pos:s])
        bullets = []
        for item in split_items(inner):
            item = itemize_to_md(item, la, level + 1)
            lines = [l.strip() for l in item.strip().split("\n")]
            lines = [l for l in lines if l]
            first = "  " * level + "- " + (lines[0] if lines else "")
            rest = ["  " * level + "  " + l if not l.startswith("-") else "  " * level + "  " + l for l in lines[1:]]
            # nested bullets are already indented relative to level+1; re-indent to sit under this item
            rest = [("  " * level + "  " + l.lstrip()) if l.lstrip().startswith("- ") and l.startswith("  " * (level + 1)) else l for l in rest]
            bullets.append("\n".join([first] + rest))
        out.append("\n" + "\n".join(bullets) + "\n")
        pos = i
    return "".join(out)

def inline_to_md(tex, la, bib, cited):
    t = tex
    # editorial residue
    for m in re.finditer(r"\\hl\{", t):
        warn(la, "stripped \\hl note: " + t[m.end(): matching(t, m.end() - 1) - 1].strip()[:80])
    t = re.sub(r"\\hl\{", "{", t)
    def color_block(m):
        if "Appendix" not in m.group(1): warn(la, "stripped red text: " + m.group(1).strip()[:80])
        return ""
    t = re.sub(r"\\color\{red\}(.*?)\\color\{black\}", color_block, t, flags=re.S)
    # citations, footnotes, links
    def cite(m):
        out = []
        for key in m.group(1).split(","):
            key = key.strip()
            if key not in bib: warn(la, f"unknown cite key {key}"); out.append(f"[{key}]"); continue
            cited.append(key)
            e = bib[key]; url = e.get("url") or (f"https://doi.org/{e['doi']}" if e.get("doi") else "")
            out.append(f"[{cite_inline(e)}]({url})" if url else cite_inline(e))
        return " ".join(out)
    t = re.sub(r"\\cite\{([^}]*)\}", cite, t)
    t = re.sub(r"\\footnote\{\s*(https?://[^}\s]+)\s*\}", lambda m: f" ([link]({m.group(1)}))", t)
    t = re.sub(r"\\footnote\{([^}]*)\}", r" (\1)", t)
    t = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", r"[\2](\1)", t)
    t = re.sub(r"\\url\{([^}]*)\}", r"<\1>", t)
    # ids and run-in headings
    t = re.sub(r"\\(?:ilo|la)\{(\w+)\}", r"\1", t)
    t = re.sub(r"\s*\\paragraph\*?\{(.*?)\}\s*", lambda m: f"\n\n**{strip_fmt(m.group(1))}.** ", t)
    # simple formatting (innermost first, a few passes for nesting)
    for _ in range(3):
        t = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", t)
        t = re.sub(r"\\(?:emph|textit)\{([^{}]*)\}", r"*\1*", t)
        t = re.sub(r"\\underline\{([^{}]*)\}", r"<u>\1</u>", t)
        t = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", t)
    # quotes, dashes, escapes
    t = re.sub(r"`(\S+)`", "\x00\\1\x00", t)                # `code` written markdown-style in the tex; protect
    t = t.replace("``", "“").replace("''", "”")
    t = re.sub(r"`([^`\n]*?)'", r"‘\1’", t)                # `quoted' → ‘quoted’
    t = t.replace("`", "‘").replace("\x00", "`")
    t = re.sub(r"(?<!-)---(?!-)", "—", t)
    t = re.sub(r"(?<!-)--(?!-)", "–", t)
    t = t.replace(r"\&", "&").replace(r"\%", "%").replace(r"\_", "_").replace(r"\$", "$").replace(r"\#", "#")
    t = re.sub(r"\\(?:ldots|dots)\b", "…", t)
    t = t.replace("~", " ").replace(r"\\", "\n")
    t = re.sub(r"\\(?:small|footnotesize|centering|noindent)\b", "", t)
    t = t.replace(r"\times", "×").replace(r"\sim", "~")
    t = re.sub(r"\$([^$]*)\$", r"\1", t)
    for cmd in sorted(set(re.findall(r"\\[a-zA-Z]+", t))):
        warn(la, f"unconverted LaTeX command {cmd}")
    return t

def strip_fmt(s):
    return re.sub(r"\\(?:textbf|emph|textit)\{([^{}]*)\}", r"\1", s)

def tidy(md):
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"(?<=\S)[ \t]{2,}", " ", md)   # collapse runs of spaces, keep list indentation
    md = re.sub(r"\n +(?=[^\s-])", "\n", md)   # unindent wrapped prose lines (not bullets)
    return md.strip()

def to_md(tex, la, bib, cited):
    return tidy(inline_to_md(itemize_to_md(strip_comments(tex), la), la, bib, cited))

def flatten(md):
    """One-line form of a converted field, for frontmatter scalars."""
    lines = [l.strip() for l in md.split("\n") if l.strip()]
    lines = [re.sub(r"^-\s+", "", l) for l in lines]
    return re.sub(r"\s+", " ", "; ".join(lines)).strip()

# --------------------------------------------------------------------- parsing

FIELDS = ["Keywords", "Related ILOs", "Type of activity", "Duration", "Prerequisites", "Resources", "Assessment", "Scale"]

def parse_section(tex):
    tex = strip_comments(tex)
    tex = tex.split(r"\subsection{Activities Validation Focus Group}")[0]
    parts = re.split(r"\\paragraph\{\\textbf\{(LA\d\d)\.\s*", tex)[1:]
    acts = {}
    for i in range(0, len(parts), 2):
        la, rest = parts[i], parts[i + 1]
        end = matching("{" + rest, 0) - 1          # heading runs to the brace closing \textbf{
        heading = rest[:end - 1].strip()
        after = rest[end + 1:]                      # skip the closing brace of \paragraph{
        box = re.search(r"\\begin\{activitybox\}\{\\latitle\{LA\d\d\}\{(.*?)\}\}(.*?)\\end\{activitybox\}", after, re.S)
        if not box: sys.exit(f"{la}: no activitybox found")
        desc, box_title, meta = after[:box.start()], box.group(1), box.group(2)
        tail = after[box.end():].strip()
        if tail: warn(la, "text after the box ignored: " + re.sub(r"\s+", " ", tail)[:80])
        fields = {}
        for f in FIELDS:
            m = re.search(r"\\item \\textbf\{" + re.escape(f) + r":\}(.*?)(?=\n\s*\\item \\textbf\{|\\end\{activitymetadata\})", meta, re.S)
            fields[f] = m.group(1).strip() if m else ""
            if not m: warn(la, f"missing field {f}")
        acts[la] = dict(id=la, heading=heading, box_title=box_title, desc=desc, fields=fields)
    return acts

def split_type(type_str):
    t = type_str.lower()
    setting = [s for s, k in [("In-class", "in-class"), ("In-lab", "in-lab"), ("Pre-sessional", "pre-sessional")] if k in t]
    grouping = [g for g, k in [("Individual", "individual"), ("Small groups", "small group")] if k in t]
    mode = next((m for m, k in [("Unplugged", "unplugged"), ("Digital", "digital"), ("Offline", "offline")] if k in t), None)
    return setting, grouping, mode

def q(s): return json.dumps(s, ensure_ascii=False)
def qlist(xs, bare=False): return "[" + ", ".join(x if bare else q(x) for x in xs) + "]"

def render(a, bib, stamp, existing):
    la, f = a["id"], a["fields"]
    cited = []
    if strip_fmt(a["heading"]) != a["box_title"]:
        warn(la, f"heading title differs from box title; using heading. box='{a['box_title']}'")
    title = flatten(to_md(a["heading"], la, bib, cited))
    keywords = [k.strip() for k in flatten(to_md(f["Keywords"], la, bib, cited)).split(",") if k.strip()]
    related = ID_RE.findall(f["Related ILOs"])
    prereq_md = to_md(f["Prerequisites"], la, bib, cited)
    prereq_ilos = [i for i in ID_RE.findall(prereq_md) if i not in related]
    type_str = flatten(to_md(f["Type of activity"], la, bib, cited))
    setting, grouping, mode = split_type(type_str)
    duration = flatten(to_md(f["Duration"], la, bib, cited))
    assessment = flatten(to_md(f["Assessment"], la, bib, cited))
    assessed = not re.match(r"(no|none)\b", assessment, re.I)
    scale = flatten(to_md(f["Scale"], la, bib, cited))
    resources_md = to_md(f["Resources"], la, bib, cited)
    desc_md = to_md(a["desc"], la, bib, cited)
    exp = existing.get("expanded_version")
    status = existing.get("status")

    fm = ["---", f"id: {la}", f"title: {q(title)}", f"keywords: {qlist(keywords)}",
          f"related_ilos: {qlist(related, bare=True)}", f"prerequisite_ilos: {qlist(prereq_ilos, bare=True)}",
          f"type: {q(type_str)}", f"setting: {qlist(setting)}", f"grouping: {qlist(grouping)}",
          f"mode: {mode or 'null'}", f"duration: {q(duration)}", f"assessment: {q(assessment)}",
          f"assessed: {'true' if assessed else 'false'}", f"scale: {q(scale)}",
          f"expanded_version: {q(exp) if exp else 'null'}"]
    if status: fm.append(f"status: {q(status)}")
    fm.append("---")

    def as_bullets(md):
        return md if md.startswith("- ") else "- " + md
    body = [f"<!-- {stamp} -->", "", f"# {title}", "",
            f"**Related ILOs:** {', '.join(related)}", "",
            f"**Type:** {type_str} · **Duration:** {duration} · **Scale:** {scale}", ""]
    if exp:
        body += [f"> Expanded version: [{exp}]({exp})" if not exp.startswith("http") else f"> Expanded version: <{exp}>", ""]
    body += ["## Description", "", desc_md, "", "## Keywords", "", ", ".join(keywords), "",
             "## Prerequisites", "", as_bullets(prereq_md), "", "## Resources", "", as_bullets(resources_md), "",
             "## Assessment", "", assessment, ""]
    seen = list(dict.fromkeys(cited))
    if seen:
        body += ["## References", ""] + [f"- {cite_full(bib[k])}" for k in seen] + [""]
    text = "\n".join(fm) + "\n" + "\n".join(body)
    # apply build-index's ILO-linking pass so the two scripts produce identical files
    m = build_index.FM_RE.match(text)
    rec = dict(related_ilos=related, prerequisite_ilos=prereq_ilos, _path=ACT / la / "README.md",
               _fm=text[:m.end()], _body=text[m.end():])
    return build_index.activity_readme(rec)

def existing_fm(path):
    if not path.exists(): return {}
    m = build_index.FM_RE.match(path.read_text())
    return yaml.safe_load(m.group(1)) if m else {}

def without_stamp(s):
    return re.sub(r"<!-- Imported from .*? -->\n", "", s, count=1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default=str(ROOT.parent / "report"))
    ap.add_argument("--only", default="")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    report = pathlib.Path(args.report).resolve()
    tex = (report / SECTION).read_text()
    try:
        commit = subprocess.run(["git", "-C", str(report), "log", "-1", "--format=%h %ad", "--date=short", "--", SECTION],
                                capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit = "unknown commit"
    stamp = (f"Imported from the WG11 report, {SECTION} (Overleaf commit {commit}) by scripts/import-from-report.py. "
             "The report is the source of truth: edit it there and re-run the import; hand edits here are overwritten.")
    bib = load_bib(report)
    acts = parse_section(tex)
    only = {x.strip() for x in args.only.split(",") if x.strip()}
    changed, wrote = [], []
    for la, a in sorted(acts.items()):
        if only and la not in only: continue
        path = ACT / la / "README.md"
        new = render(a, bib, stamp, existing_fm(path))
        old = path.read_text() if path.exists() else ""
        if without_stamp(old) != without_stamp(new):
            changed.append(la)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(new); wrote.append(la)
    for w in warnings: print("warning:", w, file=sys.stderr)
    if args.check:
        print("out of sync with the report:", ", ".join(changed) if changed else "nothing")
        sys.exit(1 if changed else 0)
    print(f"imported {len(acts)} activities from {commit}; rewrote {len(wrote)}:", ", ".join(wrote) or "nothing changed")

if __name__ == "__main__":
    main()
