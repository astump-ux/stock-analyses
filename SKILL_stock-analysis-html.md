---
name: stock-analysis-html
description: >
  Erstellt professionelle Aktienanalysen im HTML-Format nach dem "Aktienanalyse Canvas v2.2"
  Design-System. Verwende diesen Skill IMMER wenn der User eine Aktienanalyse, Stock-Report,
  Investment-These oder Unternehmensanalyse als HTML-Dokument anfordert – auch wenn er nur
  "analysiere Aktie X" sagt. Der Skill liefert das vollständige CSS/HTML-Gerüst, alle
  Design-Tokens, Komponenten und Formatierungsregeln, damit jede neue Analyse visuell
  identisch und konsistent mit der Referenz-Analyse (Xiaomi, März 2026) aussieht.
---

# Stock Analysis HTML Format Skill

Dieses Dokument definiert das komplette Design-System, alle HTML-Komponenten und
Formatierungsregeln für professionelle Aktienanalysen im Canvas-v2.2-Format.

Das visuelle Referenz-Dokument ist: **Xiaomi (1810.HK) Aktienanalyse, 03. März 2026**

---

## 1. Pflicht-Workflow

1. Diese SKILL.md zuerst lesen
2. Alle 13 Sektionen des Aktienanalyse Canvas v2.2 durcharbeiten
3. Das vollständige HTML-Dokument in einer einzigen Datei generieren
4. Ausgabe nach `/mnt/user-data/outputs/[TICKER]_Aktienanalyse_Canvas_v2.2.html`
5. HTML-Datei via Git nach `astump-ux/stock-analyses` pushen (siehe GitHub-Push Skill)
6. **Kerndaten-JSON ausgeben** (siehe Abschnitt 11) — zum Kopieren in Portfolio-App → Verwalten → "Analyse deployen"

---

## 2. CSS Custom Properties (Root Variables)

```css
:root {
  --primary: #FF6900;      /* Akzentfarbe – je nach Unternehmen/Sektor anpassen */
  --primary-dark: #cc5400;
  --bg: #0f0f12;
  --bg-card: #1a1a1f;
  --bg-card2: #22222a;
  --border: #2e2e38;
  --text: #e8e8ec;
  --text-muted: #888898;
  --text-dim: #555566;
  --green: #22c55e;
  --red: #ef4444;
  --yellow: #f59e0b;
  --blue: #3b82f6;
  --purple: #8b5cf6;
  --teal: #14b8a6;
}
```

### Primärfarbe je Sektor:
| Sektor              | --primary  | Header-Gradient-Von  | Header-Gradient-Mitte |
|---------------------|------------|----------------------|------------------------|
| Tech / Consumer     | `#FF6900`  | `#1a0800`            | `#2a1000`              |
| Pharma / Healthcare | `#3b82f6`  | `#00081a`            | `#001028`              |
| Energie / Rohstoffe | `#22c55e`  | `#001a08`            | `#002810`              |
| Finance / Banking   | `#8b5cf6`  | `#0e0018`            | `#1a0028`              |
| Industrie           | `#14b8a6`  | `#001a18`            | `#002820`              |

---

## 3. Vollständiges CSS-Template

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg); color: var(--text); font-size: 15px; line-height: 1.7;
}
.header {
  background: linear-gradient(135deg, #1a0800 0%, #2a1000 40%, #0f0f12 100%);
  border-bottom: 1px solid var(--primary);
  padding: 36px 40px 28px; display: flex; justify-content: space-between;
  align-items: flex-start; flex-wrap: wrap; gap: 20px;
}
.header-left h1 { font-size: 32px; font-weight: 700; color: white; letter-spacing: -0.5px; }
.header-left h1 span { color: var(--primary); }
.header-left .subtitle { color: var(--text-muted); font-size: 14px; margin-top: 4px; }
.header-right { text-align: right; }
.price-tag { font-size: 38px; font-weight: 800; color: var(--primary); line-height: 1; }
.price-meta { color: var(--text-muted); font-size: 13px; margin-top: 4px; }
.price-change { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 13px; font-weight: 600; margin-top: 4px; }
.price-change.up   { background: rgba(34,197,94,0.15); color: var(--green); }
.price-change.down { background: rgba(239,68,68,0.15); color: var(--red); }
.nav {
  background: var(--bg-card); border-bottom: 1px solid var(--border);
  padding: 0 40px; display: flex; gap: 0; overflow-x: auto;
  position: sticky; top: 0; z-index: 100;
}
.nav a { color: var(--text-muted); text-decoration: none; padding: 14px 16px; font-size: 13px; font-weight: 500; white-space: nowrap; border-bottom: 2px solid transparent; transition: all 0.2s; }
.nav a:hover { color: var(--primary); border-bottom-color: var(--primary); }
.main { max-width: 1100px; margin: 0 auto; padding: 32px 40px 60px; }
.kpi-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; margin-bottom: 32px; }
.kpi-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; }
.kpi-label { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
.kpi-value { font-size: 22px; font-weight: 700; color: white; margin-top: 4px; }
.kpi-sub   { font-size: 12px; color: var(--text-muted); margin-top: 2px; }
.kpi-value.green  { color: var(--green); }
.kpi-value.red    { color: var(--red); }
.kpi-value.orange { color: var(--primary); }
.section { background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 24px; overflow: hidden; }
.section-header { background: var(--bg-card2); padding: 16px 24px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--border); }
.section-number { background: var(--primary); color: white; width: 28px; height: 28px; border-radius: 6px; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.section-title  { font-size: 16px; font-weight: 700; color: white; }
.section-score  { margin-left: auto; font-size: 14px; font-weight: 700; color: var(--primary); }
.section-note   { font-size: 12px; color: var(--text-dim); background: rgba(46,46,56,0.4); border-radius: 4px; padding: 4px 10px; margin-left: auto; }
.section-body   { padding: 20px 24px; }
p { margin-bottom: 12px; color: var(--text); }
p:last-child { margin-bottom: 0; }
h3 { font-size: 14px; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px; margin: 20px 0 8px; }
h3:first-child { margin-top: 0; }
.table-wrap { overflow-x: auto; margin: 16px 0; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th { background: var(--bg-card2); color: var(--text-muted); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); }
td { padding: 10px 12px; border-bottom: 1px solid rgba(46,46,56,0.5); color: var(--text); }
tr:last-child td { border-bottom: none; }
tr:hover td { background: rgba(255,105,0,0.04); }
.beat    { color: var(--green);  font-weight: 600; }
.miss    { color: var(--red);    font-weight: 600; }
.neutral { color: var(--yellow); font-weight: 600; }
.badge        { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
.badge-green  { background: rgba(34,197,94,0.15);  color: var(--green); }
.badge-red    { background: rgba(239,68,68,0.15);  color: var(--red); }
.badge-yellow { background: rgba(245,158,11,0.15); color: var(--yellow); }
.badge-blue   { background: rgba(59,130,246,0.15); color: var(--blue); }
.badge-orange { background: rgba(255,105,0,0.15);  color: var(--primary); }
.event-item { display: flex; gap: 12px; padding: 10px 0; border-bottom: 1px solid rgba(46,46,56,0.5); align-items: flex-start; }
.event-item:last-child { border-bottom: none; }
.event-dot  { width: 8px; height: 8px; border-radius: 50%; margin-top: 7px; flex-shrink: 0; }
.dot-green  { background: var(--green); }
.dot-red    { background: var(--red); }
.dot-yellow { background: var(--yellow); }
.event-label { font-weight: 600; color: white; }
.event-text  { font-size: 14px; color: var(--text); }
.risk-item   { background: var(--bg-card2); border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; margin-bottom: 10px; }
.risk-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.risk-title  { font-weight: 600; color: white; font-size: 14px; }
.score-bar       { display: flex; align-items: center; gap: 10px; }
.score-bar-track { flex: 1; height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
.score-bar-fill  { height: 100%; border-radius: 3px; background: linear-gradient(90deg, var(--primary), #ff9500); }
.score-num       { font-weight: 700; color: var(--primary); font-size: 15px; min-width: 32px; }
.bull-bear-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
@media(max-width: 700px) { .bull-bear-grid { grid-template-columns: 1fr; } }
.bull-card { background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.2); border-radius: 10px; padding: 16px; }
.bear-card { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2); border-radius: 10px; padding: 16px; }
.bull-card h4 { color: var(--green); margin-bottom: 10px; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
.bear-card h4 { color: var(--red);   margin-bottom: 10px; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
.rating-box { background: linear-gradient(135deg, rgba(255,105,0,0.12), rgba(255,105,0,0.04)); border: 1px solid rgba(255,105,0,0.3); border-radius: 12px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; margin: 20px 0; }
.rating-item label { font-size: 11px; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px; display: block; margin-bottom: 4px; }
.rating-item .val  { font-size: 20px; font-weight: 800; color: white; }
.rating-item .val.buy  { color: var(--green); }
.rating-item .val.hold { color: var(--yellow); }
.rating-item .val.sell { color: var(--red); }
.trigger-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }
@media(max-width: 700px) { .trigger-grid { grid-template-columns: 1fr; } }
.trigger-card      { background: var(--bg-card2); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }
.trigger-card h5   { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; }
.trigger-card.buy  h5 { color: var(--green); }
.trigger-card.sell h5 { color: var(--red); }
.trigger-list    { font-size: 13px; color: var(--text); list-style: none; padding: 0; }
.trigger-list li { margin-bottom: 6px; padding-left: 14px; position: relative; }
.trigger-list li::before { content: "→"; position: absolute; left: 0; }
.investor-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
@media(max-width: 600px) { .investor-grid { grid-template-columns: 1fr; } }
.investor-yes { background: rgba(34,197,94,0.08); border: 1px solid rgba(34,197,94,0.2); border-radius: 8px; padding: 12px; }
.investor-no  { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2); border-radius: 8px; padding: 12px; }
.investor-yes h5 { color: var(--green); font-size: 12px; text-transform: uppercase; margin-bottom: 8px; }
.investor-no  h5 { color: var(--red);   font-size: 12px; text-transform: uppercase; margin-bottom: 8px; }
.investor-yes li, .investor-no li { font-size: 13px; color: var(--text); margin-bottom: 4px; list-style: none; padding-left: 14px; position: relative; }
.investor-yes li::before { content: "✓"; position: absolute; left: 0; color: var(--green); }
.investor-no  li::before { content: "✗"; position: absolute; left: 0; color: var(--red); }
.geo-grid   { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 10px; margin: 12px 0; }
.geo-card   { background: var(--bg-card2); border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; }
.geo-region { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
.geo-pct    { font-size: 20px; font-weight: 700; color: white; }
.geo-note   { font-size: 12px; color: var(--text-muted); }
.outlook-card { background: var(--bg-card2); border: 1px solid var(--border); border-left: 3px solid var(--primary); border-radius: 0 8px 8px 0; padding: 16px; margin-bottom: 14px; }
.outlook-card h4 { color: white; font-size: 14px; margin-bottom: 8px; }
.outlook-card .when-then { font-size: 13px; color: var(--text); margin-top: 8px; }
.outlook-card .when-then strong { color: var(--primary); }
.source { font-size: 11px; color: var(--text-dim); margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(46,46,56,0.5); }
.source a { color: var(--text-dim); }
.disclaimer { background: var(--bg-card2); border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; font-size: 12px; color: var(--text-dim); margin-top: 32px; }
.alert-box { background: rgba(255,105,0,0.08); border: 1px solid rgba(255,105,0,0.2); border-radius: 6px; padding: 10px 14px; margin-bottom: 16px; font-size: 13px; }
.divider   { border: none; border-top: 1px solid var(--border); margin: 16px 0; }
.pill      { display: inline-block; background: rgba(255,105,0,0.12); color: var(--primary); border-radius: 4px; padding: 1px 7px; font-size: 13px; font-weight: 600; }
```

---

## 4. HTML-Grundgerüst

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[TICKER] – Aktienanalyse Canvas v2.2</title>
  <style>/* [SECTION 2 ROOT VARS + SECTION 3 FULL CSS] */</style>
</head>
<body>

  <div class="header">
    <div class="header-left">
      <h1>[Unternehmensname] <span>[TICKER.EXCHANGE]</span></h1>
      <div class="subtitle">Aktienanalyse Canvas v2.2 · Stand: [DATUM] · [BÖRSE] · Sektor: [SEKTOR]</div>
      <div style="margin-top:10px; display:flex; gap:8px; flex-wrap:wrap;">
        <span class="badge badge-orange">[Segment 1]</span>
        <span class="badge badge-blue">[Segment 2]</span>
      </div>
    </div>
    <div class="header-right">
      <div class="price-tag">[WÄHRUNG] [KURS]</div>
      <div class="price-meta">Schlusskurs [DATUM] · [BÖRSE]</div>
      <div class="price-change [up|down]">[▲▼] [ÄNDERUNG]</div>
      <div style="margin-top:6px; font-size:12px; color:var(--text-muted);">52W: [LOW] – [HIGH]</div>
    </div>
  </div>

  <nav class="nav">
    <a href="#s1">1. Geschäftsmodell</a>
    <a href="#s2">2. Burggraben</a>
    <a href="#s3">3. Quartale</a>
    <a href="#s4">4. Wachstum</a>
    <a href="#s5">5. Bewertung</a>
    <a href="#s6">6. Cashflow</a>
    <a href="#s7">7. Peers</a>
    <a href="#s8">8. News</a>
    <a href="#s9">9. Technisch</a>
    <a href="#s10">10. Risiken</a>
    <a href="#s11">11. Scoring</a>
    <a href="#s12">12. Fazit</a>
    <a href="#s13">13. Outlook</a>
  </nav>

  <div class="main">

    <!-- KPI OVERVIEW: 6–8 Cards (Kurs / Marktkapitalisierung / P/E / EV-EBITDA / Bruttomarge / ROE / Nächste Earnings / Konsens) -->
    <div class="kpi-grid" style="margin-top:24px;">
      <div class="kpi-card"><div class="kpi-label">Kurs</div><div class="kpi-value [red|green]">[KURS]</div><div class="kpi-sub">[WÄHRUNG] · [DATUM]</div></div>
      <!-- weitere KPI-Cards ... -->
    </div>

    <!-- SEKTIONEN 1–13 -->

    <div class="disclaimer">⚠️ <strong>Disclaimer:</strong> Diese Analyse dient ausschließlich zu Informationszwecken...</div>
  </div>
</body>
</html>
```

---

## 5. Sektions-Template (alle 13 Sektionen)

```html
<div class="section" id="s[N]">
  <div class="section-header">
    <div class="section-number">[N]</div>
    <div class="section-title">[Titel]</div>
    <!-- NUR EINES der folgenden: -->
    <div class="section-score">Score: X/10</div>
    <!-- ODER: -->
    <div class="section-note">Quellen ≤ X Monate</div>
  </div>
  <div class="section-body">
    <h3>Unterabschnitt-Titel</h3>
    <p>Fließtext-Absatz (3–5 Sätze)...</p>
    <div class="table-wrap"><table>...</table></div>
    <div class="source">Quellen: [Quelle 1] ([Datum]); [Quelle 2]</div>
  </div>
</div>
```

---

## 6. Alle Komponenten-Templates

### Event-Item (Sektion 8 – News)
```html
<div class="event-item">
  <div class="event-dot dot-green"></div>  <!-- dot-green | dot-red | dot-yellow -->
  <div>
    <div class="event-label">DD.MM.YYYY – Titel <span class="badge badge-green">Positiv</span></div>
    <div class="event-text">Beschreibung. Quelle: Reuters/Bloomberg, DD.MM.YYYY</div>
  </div>
</div>
```

### Risk-Item (Sektion 10)
```html
<div class="risk-item">
  <div class="risk-header">
    <div class="risk-title">⚡ Risiko-Titel</div>
    <div><span class="badge badge-red">Hoch</span> <span class="badge badge-orange">Auswirkung: Mittel</span></div>
  </div>
  <div class="event-text">Beschreibung. Wahrscheinlichkeit: X%.</div>
</div>
```

### Score-Bar (Sektion 11) — width = Score × 10%
```html
<div class="score-bar">
  <div class="score-bar-track">
    <div class="score-bar-fill" style="width:70%"></div>  <!-- 7/10 = 70% -->
  </div>
  <span class="score-num">7</span>
</div>
```

### Gesamt-Score-Zeile (Sektion 11 – letzte Tabellenzeile)
```html
<tr style="background:rgba(255,105,0,0.08);">
  <td><strong>⌀ Gesamtscore</strong></td>
  <td><strong>[X.Y]/10</strong></td>
  <td>
    <div class="score-bar">
      <div class="score-bar-track">
        <div class="score-bar-fill" style="width:[X.Y*10]%; background:linear-gradient(90deg,var(--primary),#ffd700);"></div>
      </div>
      <span class="score-num" style="color:var(--primary);">[X.Y]</span>
    </div>
  </td>
  <td>Zusammenfassende Begründung</td>
</tr>
```

### Bull/Bear Cards (Sektion 12)
```html
<div class="bull-bear-grid">
  <div class="bull-card">
    <h4>🐂 Das Bullische Narrativ</h4>
    <p>Säule 1: [Konkrete Zahl/Metrik]. [Erklärung]. [Katalysator].</p>
    <p>Säule 2: [Konkrete Zahl/Metrik]. [Erklärung]. [Struktureller Vorteil].</p>
    <p>Säule 3: [Bewertungsargument mit PEG/Multiple]. [Upside-Rechnung].</p>
  </div>
  <div class="bear-card">
    <h4>🐻 Das Bärische Narrativ</h4>
    <p>Risiko 1: [Konkretes Risiko]. Falls X eintritt → EBITDA-Marge sinkt von Y% auf Z%.</p>
    <p>Risiko 2: [Wettbewerbsdruck]. [Quantifizierte Auswirkung].</p>
    <p>Risiko 3: [Technisch/Timing]. P/E [X]x ist nicht billig wenn Wachstum auf [Y]% fällt.</p>
  </div>
</div>
```

### Rating-Box (Sektion 12)
```html
<div class="rating-box">
  <!-- Gradient in background an --primary anpassen! -->
  <div class="rating-item"><label>Rating</label><div class="val [buy|hold|sell]">[✓ KAUFEN | = HALTEN | ✗ VERKAUFEN]</div></div>
  <div class="rating-item"><label>Zielkurs (12–18M)</label><div class="val">[WÄHRUNG X–Y]</div></div>
  <div class="rating-item"><label>Zeithorizont</label><div class="val">[X–Y Jahre]</div></div>
  <div class="rating-item"><label>Downside</label><div class="val" style="color:var(--red);">–X%</div></div>
  <div class="rating-item"><label>Upside</label><div class="val" style="color:var(--green);">+Y%</div></div>
  <div class="rating-item"><label>Risk/Reward</label><div class="val green">1:Z</div></div>
</div>
```

### Trigger-Cards (Sektion 12 – Falsifikation)
```html
<div class="trigger-grid">
  <div class="trigger-card sell">
    <h5>🔴 Bearish Trigger → Verkaufen / Reduzieren</h5>
    <ul class="trigger-list">
      <li>Bedingung X passiert → sofort verkaufen</li>
      <li>Metric Y fällt unter Z → Position reduzieren</li>
    </ul>
  </div>
  <div class="trigger-card buy">
    <h5>🟢 Bullish Trigger → Nachkaufen / Einsteigen</h5>
    <ul class="trigger-list">
      <li>Bedingung A passiert → nachkaufen</li>
      <li>Metric B steigt über C → Position aufbauen</li>
    </ul>
  </div>
</div>
```

### Investor-Cards (Sektion 12)
```html
<div class="investor-grid">
  <div class="investor-yes">
    <h5>✅ Geeignet für</h5>
    <ul><li>Growth Investors</li><li>Quality Growth</li><li>Contrarian</li></ul>
  </div>
  <div class="investor-no">
    <h5>❌ NICHT geeignet für</h5>
    <ul><li>Value Investors</li><li>Income Investors</li><li>Kurzfristige Trader</li></ul>
  </div>
</div>
```

### Einstieg-Tabelle (Sektion 12)
```html
<div class="table-wrap">
  <table>
    <thead><tr><th>Investorentyp</th><th>Empfehlung</th><th>Begründung</th></tr></thead>
    <tbody>
      <tr><td><strong>Konservativ</strong></td><td><span class="badge badge-yellow">Warten / Tranchiert</span></td><td>Abwarten auf [konkreten Katalysator]</td></tr>
      <tr><td><strong>Moderat</strong></td>    <td><span class="badge badge-orange">Tranchiert einsteigen</span></td><td>X% jetzt, Y% nach Bestätigung</td></tr>
      <tr><td><strong>Aggressiv</strong></td>  <td><span class="badge badge-green">Jetzt kaufen</span></td><td>Risk/Reward [X:Y] bei aktuellem Kurs</td></tr>
      <tr><td><strong>Langfristig</strong></td><td><span class="badge badge-green">Kaufen & Halten</span></td><td>[Strukturelles Wachstumsthema]</td></tr>
    </tbody>
  </table>
</div>
```

### Outlook-Card (Sektion 13) – immer genau 3 Cards
```html
<div class="outlook-card">
  <h4>📊 Event N: [Titel] – [voraussichtlicher Zeitraum]</h4>
  <p>Beschreibung des Events und warum es für das Investmentnarrativ entscheidend ist.</p>
  <div class="when-then">
    <strong>Wenn:</strong> [konkrete Bedingung mit Schwellenwert] → [konkrete Handlungsempfehlung mit Begründung].<br><br>
    <strong>Wenn:</strong> [alternative Bedingung] → [alternative Handlungsempfehlung].
  </div>
</div>
```

### Geography Cards (Sektion 4)
```html
<div class="geo-grid">
  <div class="geo-card">
    <div class="geo-region">Region</div>
    <div class="geo-pct">XX%</div>
    <div class="geo-note">Wachstum / Kommentar</div>
  </div>
  <!-- weitere geo-cards... -->
</div>
```

### Alert-Box (bei Nicht-US-Aktien in Sektion 3 und 5)
```html
<div class="alert-box">
  ⚠️ <strong>Hinweis:</strong> Da [TICKER] an der [BÖRSE] notiert ist, sind keine finviz.com-Daten verfügbar.
  Alle Kennzahlen stammen von investing.com, Yahoo Finance und der Unternehmens-IR (Stand: [DATUM]).
</div>
```

---

## 7. Sektion-spezifische Pflichtregeln

| Sektion | Pflichtregeln |
|---|---|
| S3 – Quartale | Bei Nicht-US-Aktien: `alert-box` mit Datenquellen-Hinweis. Beat-Ratio in `section-score` |
| S4 – Wachstum | `geo-grid` für geografische Verteilung |
| S8 – News | Immer 3 `h3`: "Ebene 1: Unternehmen", "Ebene 2: Branche", "Ebene 3: Makro" |
| S9 – Technisch | Mini-KPI-Grid: `minmax(130px, 1fr)` für 7 Werte: Kurs/SMA20/SMA50/SMA200/RSI/52W-High/MACD |
| S11 – Scoring | Gesamt-Zeile mit `rgba(255,105,0,0.08)` Hintergrund + Gold-Gradient |
| S12 – Fazit | Reihenfolge: Bull/Bear → Eigene Einschätzung → Zeithorizont-Tabelle → Kernthese → Rating-Box → Trigger-Grid → Investor-Grid → Einstieg-Tabelle |
| S13 – Outlook | Genau 3 `outlook-card` mit Wenn/Dann – nie mehr, nie weniger |

---

## 8. Qualitätschecklist vor Finalisierung

```
☐ Alle 13 Sektionen vorhanden mit id="s1" bis id="s13"?
☐ Sticky-Nav mit allen 13 href-Ankern?
☐ KPI-Overview-Grid direkt unter der Nav mit margin-top:24px?
☐ .source-Block in jeder Sektion?
☐ Scores (section-score) in Sektionen 2, 3 (Beat-Ratio), 4, 5, 6, 7, 9, 10, 11?
☐ Ø Gesamtscore in Sektion 11 korrekt berechnet (Durchschnitt aller Einzelscores)?
☐ Rating-Box: Klasse buy/hold/sell korrekt gesetzt?
☐ Genau 3 Outlook-Cards in Sektion 13?
☐ Disclaimer am Ende?
☐ --primary und Header-Gradient-Farben zu Unternehmenssektor angepasst?
☐ Dateiname: [TICKER]_Aktienanalyse_Canvas_v2.2.html
☐ HTML via Git nach astump-ux/stock-analyses gepusht?
☐ Kerndaten-JSON (Abschnitt 11) ausgegeben und bereit zum Kopieren?
```

---

## 9. Häufige Fehler

| ❌ Falsch | ✅ Richtig |
|---|---|
| `<ul><li>` für Fließtext-Sektionen | `<p>`-Tags (3–5 Sätze pro Absatz) |
| `<table>` ohne `<div class="table-wrap">` | Immer `<div class="table-wrap"><table>...` |
| Score-Bar width als Zahl: `style="width:7"` | `style="width:70%"` (Score × 10) |
| `.section-score` + `.section-note` gleichzeitig | Nur EINES von beiden pro Section-Header |
| Rating-Box bei HALTEN mit `.val.buy` | `.val.hold` (→ gelbe Farbe) |
| Outlook-Card ohne `.when-then` | Immer `<div class="when-then"><strong>Wenn:</strong>...` |
| `tr:hover` Farbe nicht an --primary angepasst | `rgba([PRIMARY_RGB], 0.04)` |
| Header-Gradient nicht zu --primary passend | Gradient-Farben aus Tabelle in Abschnitt 2 |

---

## 11. Kerndaten-JSON für Portfolio-App

Nach dem GitHub-Push die folgenden Kerndaten als kopierbaren JSON-Block ausgeben.
Der User kopiert diesen Block in die Portfolio-App → Verwalten Tab → "Analyse deployen" → Paste & Deploy.

**Pflichtfelder** (alle aus der fertigen Analyse befüllen):

```json
{
  "ticker": "[TICKER]",
  "name": "[Vollständiger Unternehmensname]",
  "exchange": "[Börse, z.B. NASDAQ / NYSE / XETRA / HKEX]",
  "sector": "[Sektor, z.B. Technology / Healthcare / Energy]",
  "price": "[Aktueller Kurs mit Währung, z.B. ~$185]",
  "priceDate": "[Datum des Kurses, z.B. 01.04.2026]",
  "w52": "[52W-Range, z.B. $142 – $220]",
  "scores": {
    "gm": [1-10],
    "bg": [1-10],
    "qu": [1-10],
    "wa": [1-10],
    "bw": [1-10],
    "cf": [1-10],
    "ri": [1-10],
    "ta": [1-10]
  },
  "rating": "[KAUFEN / HALTEN / VERKAUFEN]",
  "zielkurs": "[Zielkurs-Range, z.B. $210–230]",
  "upside": "[Upside in %, z.B. +24%]",
  "downside": "[Downside in %, z.B. -15%]",
  "rr": "[Risk/Reward, z.B. 1:1.6]",
  "horizont": "[Zeithorizont, z.B. 2–3 Jahre]",
  "analyseDate": "[Datum der Analyse, z.B. 01.04.2026]",
  "badges": ["[Badge 1]", "[Badge 2]"]
}
```

**Score-Mapping** (Sektionsnummern → JSON-Felder):
| Sektion | Beschreibung | JSON-Feld |
|---|---|---|
| S2 | Burggraben | `bg` |
| S3 | Operative Entwicklung (4Q) | `qu` |
| S4 | Wachstum | `wa` |
| S5 | Bewertung | `bw` |
| S6 | Cashflow & Margen | `cf` |
| S7 | Peer-Vergleich | `pe` *(optional)* |
| S9 | Technische Analyse | `ta` |
| S10 | Risiken (invertiert) | `ri` |
| S11 | Ø Gesamtscore | → wird in App berechnet |

**Hinweis:** `gm` (Geschäftsmodell) wird in der App aus Sektion 1 abgeleitet — Richtwert: solides GM = 7, starkes GM = 8–9.

---

## 10. Referenz-Dokument

Dieses Skill basiert auf der Xiaomi (1810.HK) Aktienanalyse vom 03. März 2026.
Datei: `Xiaomi_Aktienanalyse_Canvas_v2.2.html`

Bei Layout-Fragen und Unklarheiten zu Komponenten ist diese HTML-Datei
die visuelle Quelle der Wahrheit.
