import re, sys, markdown

repo = sys.argv[1]
src = open(f"{repo}/docs/PRD.md").read()
md = markdown.Markdown(extensions=["tables", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2"}})
body = md.convert(src)
body = body.replace("<li>[x] ", '<li class="done"><span class="box" aria-hidden="true">✓</span>').replace("<li>[ ] ", '<li class="todo"><span class="box" aria-hidden="true"></span>')
body = re.sub(r"<hr\s*/?>", "", body)
body = re.sub(r"^<h1[^>]*>.*?</h1>\s*<p><strong>[^<]*</strong></p>", "", body, count=1, flags=re.S)
def walk(ts):
    for t in ts:
        yield t; yield from walk(t["children"])
toc = "".join(f'<li><a href="#{t["id"]}">{t["name"]}</a></li>' for t in walk(md.toc_tokens) if t["level"] == 2)

FONT = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap"
LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="none" stroke="currentColor" stroke-width="2"/><path d="M16 5 L20 16 L16 14 L12 16 Z" fill="var(--accent)"/><path d="M16 27 L12 16 L16 18 L20 16 Z" fill="currentColor" opacity=".45"/></svg>'

html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>North PRD</title>
<!-- Generated from docs/PRD.md. Edit the Markdown, then regenerate this page. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONT}">
<style>
:root {{
  --bg: #eef3f6; --surface: #ffffff; --surface-2: #e3ebf0; --ink: #0d1b2e; --ink-2: #4a5b70;
  --line: #cfdbe3; --accent: #0f9e8a; --accent-ink: #ffffff; --accent-soft: #d5f1ec;
  --studio: #0d1b2e; --studio-ink: #e9f2f6; --studio-ink-2: #93a7bb; --aurora: #39c9a0;
  --f-display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", sans-serif;
  --f-body: "Figtree", "Helvetica Neue", Arial, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --r: 14px;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #08121f; --surface: #102036; --surface-2: #172b45; --ink: #e9f2f6; --ink-2: #93a7bb;
    --line: #23395a; --accent: #3fd2b4; --accent-ink: #062018; --accent-soft: #123d3f; --studio: #050c16;
    color-scheme: dark;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #08121f; --surface: #102036; --surface-2: #172b45; --ink: #e9f2f6; --ink-2: #93a7bb;
  --line: #23395a; --accent: #3fd2b4; --accent-ink: #062018; --accent-soft: #123d3f; --studio: #050c16;
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 80px; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: var(--f-body); font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
a {{ color: var(--accent); }}

.topbar {{ position: sticky; top: 0; z-index: 5; background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }}
.topbar-in {{ max-width: 1120px; margin: 0 auto; padding: 12px max(16px, env(safe-area-inset-right, 0px)) 12px max(16px, env(safe-area-inset-left, 0px)); display: flex; align-items: center; gap: 12px; }}
.brand {{ display: flex; align-items: center; gap: 8px; font-family: var(--f-display); font-weight: 800; font-size: 20px; letter-spacing: -0.03em; color: var(--ink); text-decoration: none; }}
.brand svg {{ width: 26px; height: 26px; }}
.tag {{ font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: var(--ink-2); border: 1px solid var(--line); border-radius: 99px; padding: 3px 9px; }}
.btn {{ margin-left: auto; border-radius: 99px; padding: 9px 16px; font-weight: 700; font-size: 14px; background: var(--accent); color: var(--accent-ink); text-decoration: none; white-space: nowrap; }}

.hero {{ background: var(--studio); color: var(--studio-ink); position: relative; overflow: hidden; }}
.hero::before {{ content: ""; position: absolute; inset: -40% -10% auto auto; width: 560px; height: 560px; border-radius: 50%; background: radial-gradient(circle, color-mix(in srgb, var(--aurora) 30%, transparent), transparent 65%); pointer-events: none; }}
.hero-in {{ position: relative; max-width: 1120px; margin: 0 auto; padding: 48px 16px 40px; }}
.eyebrow {{ font-size: 12px; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; color: var(--studio-ink-2); }}
.hero h1 {{ font-family: var(--f-display); font-size: clamp(34px, 7vw, 56px); line-height: 1.02; letter-spacing: -0.03em; margin: 8px 0 12px; font-weight: 800; }}
.hero p {{ margin: 0; color: var(--studio-ink-2); max-width: 56ch; }}

.layout {{ max-width: 1120px; margin: 0 auto; padding: 32px 16px 64px; display: grid; gap: 32px; }}
@media (min-width: 960px) {{ .layout {{ grid-template-columns: 240px minmax(0, 1fr); gap: 48px; }} }}
nav.toc {{ align-self: start; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r); padding: 16px; }}
@media (min-width: 960px) {{ nav.toc {{ position: sticky; top: 84px; max-height: calc(100vh - 100px); overflow: auto; }} }}
nav.toc summary {{ cursor: pointer; font-weight: 700; display: block; font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: var(--ink-2); margin-bottom: 8px; }}
nav.toc ol {{ margin: 0; padding: 0; list-style: none; display: grid; gap: 2px; }}
nav.toc a {{ display: block; padding: 5px 8px; border-radius: 8px; color: var(--ink); text-decoration: none; font-size: 14px; line-height: 1.35; }}
nav.toc a:hover {{ background: var(--surface-2); }}

article {{ min-width: 0; max-width: 760px; }}
article h2 {{ font-family: var(--f-display); font-size: 28px; line-height: 1.15; letter-spacing: -0.02em; margin: 48px 0 12px; padding-top: 24px; border-top: 1px solid var(--line); }}
article h2:first-of-type {{ margin-top: 32px; }}
article h3 {{ font-family: var(--f-display); font-size: 20px; letter-spacing: -0.01em; margin: 28px 0 8px; }}
article h4 {{ font-size: 12px; text-transform: uppercase; letter-spacing: .1em; color: var(--ink-2); margin: 20px 0 6px; }}
article p, article li {{ max-width: 68ch; }}
article ul, article ol {{ padding-left: 22px; }}
article li {{ margin: 4px 0; }}
article code {{ font-family: var(--f-mono); font-size: .86em; background: var(--surface-2); padding: 1px 6px; border-radius: 6px; }}
article blockquote {{ margin: 20px 0; padding: 14px 16px; background: color-mix(in srgb, var(--accent-soft) 55%, var(--surface)); border: 1px solid var(--accent); border-radius: var(--r); }}
article blockquote p {{ margin: 0; }}
.meta {{ list-style: none; padding: 0 !important; margin: 0 0 8px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px; }}
.meta li {{ margin: 0; background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 10px 12px; font-size: 14px; }}
.meta li strong {{ margin-bottom: 2px; display: block; font-size: 11px; text-transform: uppercase; letter-spacing: .1em; color: var(--ink-2); }}
.table-wrap {{ overflow-x: auto; margin: 12px 0; border: 1px solid var(--line); border-radius: var(--r); background: var(--surface); }}
table {{ border-collapse: collapse; width: 100%; min-width: 600px; font-size: 14px; }}
th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--ink-2); background: var(--surface-2); }}
tr:last-child td {{ border-bottom: 0; }}
li.done, li.todo {{ list-style: none; margin-left: -22px; display: grid; grid-template-columns: 22px 1fr; gap: 10px; align-items: start; }}
.box {{ width: 22px; height: 22px; margin-top: 2px; border-radius: 7px; border: 2px solid var(--line); display: grid; place-items: center; font-size: 12px; font-weight: 800; }}
li.done .box {{ background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }}
footer {{ border-top: 1px solid var(--line); color: var(--ink-2); font-size: 13px; text-align: center; padding: 24px 16px 40px; }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
</style>
</head>
<body>
<header class="topbar"><div class="topbar-in">
  <a class="brand" href="index.html">{LOGO}North</a>
  <span class="tag">PRD</span>
  <a class="btn" href="index.html">Open the prototype</a>
</div></header>

<section class="hero"><div class="hero-in">
  <span class="eyebrow">Product requirements document</span>
  <h1>North Card Builder</h1>
  <p>A credit card built around how you live. What the hackathon prototype does, how it works, and what's still to build.</p>
</div></section>

<div class="layout">
  <nav class="toc" aria-label="Contents"><details id="tocBox"><summary>Contents</summary><ol>{toc}</ol></details></nav>
  <script>if (matchMedia("(min-width: 960px)").matches) document.getElementById("tocBox").open = true;</script>
  <article>
{body}
  </article>
</div>
<footer>North is a fictional bank. This is a hackathon prototype and every rate, limit, fee and perk value is illustrative.</footer>
</body>
</html>
"""
html = re.sub(r"<strong>([^<]*):</strong>", r"<strong>\1</strong>", html, count=6)
# first bullet list after the title is the metadata block
html = html.replace("<ul>", '<ul class="meta">', 1)
html = re.sub(r"<table>", '<div class="table-wrap"><table>', html).replace("</table>", "</table></div>")
open(f"{repo}/prd.html", "w").write(html)
print("ok", len(html))
