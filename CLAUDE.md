# Stock Analyses — Notes for Claude

> **Audience:** Future Claude sessions working on `astump-ux/stock-analyses`.
> **Last update:** 17.05.2026

---

## What this repo is

A flat collection of `TICKER.html` files — one per analyzed stock — served via Vercel at https://v0-stock-analyses.vercel.app/TICKER.html. Each file follows the **Aktienanalyse Canvas v2.2** design system (skill at `/mnt/skills/user/stock-analysis-html/SKILL.md`).

A GitHub Action regenerates `index.json` on each HTML change, providing a machine-readable catalog at https://raw.githubusercontent.com/astump-ux/stock-analyses/main/index.json.

---

## Filename convention

**Strict:** `TICKER.html` (uppercase ticker, no suffix). e.g. `RIVN.html`, `NOW.html`, `TSMC.html`.
**Never:** `RIVN_Aktienanalyse_Canvas_v2.2.html` or similar — that's the workspace output filename only.

---

## Workflow

1. Build the HTML in `/mnt/user-data/outputs/[TICKER]_Aktienanalyse_Canvas_v2.2.html` using the canvas skill.
2. Copy/rename to `TICKER.html` in this repo and `git push`.
3. Run the parser (`/home/claude/extract.py` or the `analyse-deploy` skill) to extract Kerndaten as JSON.
4. POST JSON to `https://portfolio-canvas-ten.vercel.app/api/deploy-analysis` to register in the portfolio app.
5. **Add the ticker to `YAHOO_MAP` in the portfolio-canvas repo's `api/update-prices.js`** — otherwise it gets no live prices in the overview.

---

## Companion Repo

The portfolio overview lives at `astump-ux/portfolio-canvas`. See its `CLAUDE.md` for the full data model, price-fetching architecture, and known gotchas.

---

## Key Values from Extracted JSON

The parser pulls these out of each HTML; they must validate before the JSONBin push:

```
analyseDate, priceDate, exchange, sector, name, price, w52, badges,
rating ("KAUFEN" | "HALTEN" | "VERKAUFEN" — no prefix symbols),
zielkurs, upside, downside, rr, horizont,
scores: {gm, bg, qu, wa, bw, cf, ri, ta}  // all 8 fields, integers 1-10
```

**Datentyp-Falle:** `price`, `upside`, `downside`, `rr`, `w52`, `zielkurs`, `horizont` must be **strings** (`"~$166"`, `"+35%"`). `scores` values must be **numbers**. `events`, `badges` must be **arrays**. Wrong types crash `parseP()` in the UI and produce blank screens.

---

## Configuration Quick Reference

```
GitHub:    astump-ux/stock-analyses (branch: main)
Vercel:    https://v0-stock-analyses.vercel.app
Index:     https://raw.githubusercontent.com/astump-ux/stock-analyses/main/index.json
Skill:     /mnt/skills/user/stock-analysis-html/SKILL.md (Canvas v2.2 design system)
Parser:    /home/claude/extract.py
```
