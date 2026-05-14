---
name: analyse-deploy
description: >
  Verwende diesen Skill IMMER wenn eine fertige Aktienanalyse (neue Analyse ODER Update)
  nach GitHub/Vercel deployed werden soll und das Kerndaten-JSON für die Portfolio-App
  ausgegeben werden soll. Trigger-Phrasen: "deploy die Analyse", "pushe die Analyse",
  "publish die Analyse", "Analyse deployen", "Kerndaten-JSON ausgeben",
  "nach GitHub pushen", oder am Ende jedes Analyse-Workflows nach Sektion 13.
  WICHTIG: Immer automatisch pushen — nie auf Bestätigung warten, nie nur Download anbieten.
---

# Analyse-Deploy Skill

Dieser Skill deckt den vollständigen Publikations-Workflow ab:
GitHub-Push → Vercel-Auto-Deploy → Kerndaten-JSON für Portfolio-App.

**GRUNDREGEL: Immer automatisch pushen. Nie fragen, nie nur Download anbieten.**

---

## 1. Voraussetzungen

- HTML-Datei liegt unter `/mnt/user-data/outputs/[TICKER]_Aktienanalyse_Canvas_v2.2.html`
  ODER wurde direkt hochgeladen (dann Pfad aus `/mnt/user-data/uploads/`)
- Alle 13 Sektionen vollständig

---

## 2. GitHub-Push Analysen (astump-ux/stock-analyses)

```bash
TICKER="NOW"   # ← anpassen
TOKEN="GH_TOKEN_IN_MEMORY"
WORK_DIR="/tmp/gh_push_$$"

git clone --depth=1 \
  "https://${TOKEN}@github.com/astump-ux/stock-analyses.git" \
  "$WORK_DIR" 2>&1 | tail -1

cp "/mnt/user-data/outputs/${TICKER}_Aktienanalyse_Canvas_v2.2.html" \
   "${WORK_DIR}/${TICKER}.html"

cd "$WORK_DIR"
git config user.email "bot@claude.ai"
git config user.name "Claude Bot"
git add -A
git diff --cached --quiet && echo "Keine Änderungen." || \
  (git commit -m "Add/Update ${TICKER} Aktienanalyse Canvas v2.2" && \
   git push "https://${TOKEN}@github.com/astump-ux/stock-analyses.git" main 2>&1)
rm -rf "$WORK_DIR"
```

→ Live unter: `https://v0-stock-analyses.vercel.app/[TICKER].html`

---

## 3. GitHub-Push Portfolio-App (astump-ux/portfolio-canvas)

```bash
TOKEN="GH_TOKEN_IN_MEMORY"
WORK_DIR="/tmp/gh_app_$$"

git clone --depth=1 \
  "https://${TOKEN}@github.com/astump-ux/portfolio-canvas.git" \
  "$WORK_DIR" 2>&1 | tail -1

cp /mnt/user-data/outputs/Portfolio_Canvas_v2.2_App.html "${WORK_DIR}/index.html"

cd "$WORK_DIR"
git config user.email "bot@claude.ai"
git config user.name "Claude Bot"
git add index.html
git diff --cached --quiet && echo "Keine Änderungen." || \
  (git commit -m "[Beschreibung der Änderung]" && \
   git push "https://${TOKEN}@github.com/astump-ux/portfolio-canvas.git" main 2>&1)
rm -rf "$WORK_DIR"
```

→ Live unter: `https://portfolio-canvas-ten.vercel.app`

---

## 4. Kerndaten-JSON (nach jedem Analyse-Deploy ausgeben)

Nach dem Push diesen JSON-Block ausgeben — User kopiert in:
**Portfolio-App → Verwalten → "Analyse deployen" → Paste & Deploy**

```json
{
  "ticker": "[TICKER]",
  "name": "[Vollständiger Unternehmensname]",
  "exchange": "[NYSE / NASDAQ / XETRA / HKEX / ...]",
  "sector": "[Sektor]",
  "price": "[~$XXX]",
  "priceDate": "[TT.MM.JJJJ]",
  "w52": "[LOW – HIGH]",
  "scores": {
    "gm": 0,
    "bg": 0,
    "qu": 0,
    "wa": 0,
    "bw": 0,
    "cf": 0,
    "ri": 0,
    "ta": 0
  },
  "rating": "[KAUFEN / HALTEN / VERKAUFEN]",
  "zielkurs": "[z.B. $140–180]",
  "upside": "[z.B. +70%]",
  "downside": "[z.B. -20%]",
  "rr": "[z.B. 1:3.5]",
  "horizont": "[z.B. 2–3 Jahre]",
  "analyseDate": "[TT.MM.JJJJ]",
  "badges": ["[Badge 1]", "[Badge 2]"]
}
```

### Score-Mapping:
| JSON-Feld | Sektion | Beschreibung |
|---|---|---|
| `gm` | S1 | Geschäftsmodell (solide=7, stark=8–9) |
| `bg` | S2 | Burggraben |
| `qu` | S3 | Operative Entwicklung / 4 Quartale |
| `wa` | S4 | Wachstum |
| `bw` | S5 | Bewertung |
| `cf` | S6 | Cashflow & Kapitalqualität |
| `ri` | S10 | Risiken **invertiert** (10=kein Risiko) |
| `ta` | S9 | Technische Analyse |

---

## 5. Konfiguration

```
GitHub Token : GH_TOKEN_IN_MEMORY
GitHub User  : astump-ux
Repo Analysen: astump-ux/stock-analyses → https://v0-stock-analyses.vercel.app/[TICKER].html
Repo App     : astump-ux/portfolio-canvas → https://portfolio-canvas-ten.vercel.app
```

---

## 6. Häufige Fehler

| Problem | Fix |
|---|---|
| `Repository not found` | Token prüfen/erneuern |
| `nothing to commit` | Normal — Datei identisch |
| `non-fast-forward` | `git pull --rebase` vor Push |
| Datei nicht gefunden | Pfad prüfen: outputs/ oder uploads/ |
