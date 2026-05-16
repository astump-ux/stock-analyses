---
name: analyse-deploy
description: >
  Verwende diesen Skill IMMER wenn eine fertige Aktienanalyse (neue Analyse ODER Update)
  nach GitHub/Vercel deployed werden soll und das Kerndaten-JSON für die Portfolio-App
  ausgegeben werden soll. WICHTIG: Immer automatisch pushen — nie auf Bestätigung warten.
---

# Analyse-Deploy Skill

## KRITISCHE DATENTYP-REGELN (ZWINGEND EINHALTEN)

Alle Felder im Kerndaten-JSON MÜSSEN korrekte Datentypen haben:

| Feld | Typ | Korrekt | Falsch |
|---|---|---|---|
| `price` | String | `"~$166"` | `166` |
| `currentPrice` | String | `"166.50"` | `166.50` |
| `upside` | String | `"+35–50%"` | `35` |
| `downside` | String | `"-15%"` | `-15` |
| `rr` | String | `"1:2.5"` | `2.5` |
| `w52` | String | `"$103 – $210"` | – |
| `scores` | Objekt mit Zahlen | `{"gm":8,"bg":7,...}` | `{"gm":"8"}` |
| `events` | Array | `[]` | fehlendes Feld |
| `badges` | Array | `["Badge1"]` | fehlendes Feld |

**Niemals Zahlen für String-Felder verwenden — crash in parseP() der App!**

---

## 1. GitHub-Push Analysen (astump-ux/stock-analyses)

```bash
TICKER="NOW"
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

## 2. GitHub-Push Portfolio-App (astump-ux/portfolio-canvas)

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
  (git commit -m "[Beschreibung]" && \
   git push "https://${TOKEN}@github.com/astump-ux/portfolio-canvas.git" main 2>&1)
rm -rf "$WORK_DIR"
```

→ Live unter: `https://portfolio-canvas-ten.vercel.app`

---

## 3. Kerndaten-JSON Template (PFLICHTFORMAT)

```json
{
  "ticker": "NOW",
  "name": "ServiceNow, Inc.",
  "exchange": "NYSE",
  "sector": "Enterprise Software",
  "price": "~$166",
  "priceDate": "14.05.2026",
  "w52": "~$103 – $210",
  "scores": {
    "gm": 8,
    "bg": 8,
    "qu": 9,
    "wa": 9,
    "bw": 5,
    "cf": 9,
    "ri": 6,
    "ta": 7
  },
  "rating": "KAUFEN",
  "zielkurs": "$220–250",
  "upside": "+35–50%",
  "downside": "-15%",
  "rr": "1:2.5",
  "horizont": "2–3 Jahre",
  "analyseDate": "14.05.2026",
  "badges": ["AI Control Tower", "Workflow Platform"]
}
```

### Score-Mapping:
| JSON-Feld | Sektion |
|---|---|
| `gm` | S1 Geschäftsmodell |
| `bg` | S2 Burggraben |
| `qu` | S3 Operative Entwicklung |
| `wa` | S4 Wachstum |
| `bw` | S5 Bewertung |
| `cf` | S6 Cashflow |
| `ri` | S10 Risiken (invertiert, 10=kein Risiko) |
| `ta` | S9 Technische Analyse |

---

## 4. Konfiguration

```
GitHub User  : astump-ux
Token        : GH_TOKEN_IN_MEMORY (in Claude-Memory gespeichert)
Repo Analysen: astump-ux/stock-analyses
Vercel URL   : https://v0-stock-analyses.vercel.app/[TICKER].html
Repo App     : astump-ux/portfolio-canvas
App URL      : https://portfolio-canvas-ten.vercel.app
JSONBin ID   : 69b68c14aa77b81da9e78b7e
```

---

## 5. Häufige Fehler

| Problem | Ursache | Fix |
|---|---|---|
| Blank Screen `parseP is not a function` | price als Zahl statt String | Immer `"~$166"` nicht `166` |
| Blank Screen `filter is not a function` | events/badges fehlen | sanitizeCo() läuft automatisch |
| `nothing to commit` | Datei identisch | Normal |
| `non-fast-forward` | `git pull --rebase` vor Push |
