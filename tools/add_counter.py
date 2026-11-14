"""Add the visit counter to every built page: python tools/add_counter.py site

The counter is GoatCounter (no cookies, no personal data: page, referring site, browser, country).
The script is pinned to one published version by its hash, so the browser refuses a changed file.
It runs on the built site only, so the files in this repo stay as they were generated.
"""

import sys
from pathlib import Path

CODE = "aimpg"  # the dashboard is https://aimpg.goatcounter.com
SCRIPT = (
    f'<script data-goatcounter="https://{CODE}.goatcounter.com/count" async src="https://gc.zgo.at/count.v5.js" '
    'crossorigin="anonymous" integrity="sha384-atnOLvQb9t+jTSipvd75X2yginT4PjVbqDdlJAmxMm+wYElFmeR6EmLP5bYeoRVQ"></script>'
)
NOTE = (
    '<p style="max-width:60em;margin:2em auto 1.5em;padding:0 16px;font-size:13px;opacity:.7;text-align:center">'
    'This site counts page visits with <a href="https://www.goatcounter.com" style="color:inherit">GoatCounter</a>: '
    "no cookies and no personal data. The aimpg tool itself sends nothing.</p>"
)


def main(site: str) -> int:
    pages = sorted(p for p in Path(site).rglob("*.html") if "records" not in p.relative_to(site).parts)
    if not pages:
        print(f"no pages found under {site}")
        return 1
    for page in pages:
        text = page.read_text()
        if text.count("</body>") != 1:  # a bare file listing, not a page people land on
            print(f"skipped (no single </body>): {page}")
            continue
        page.write_text(text.replace("</body>", f"{NOTE}{SCRIPT}</body>"))
        print(f"counter added: {page}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
