import json, sys, os

ticker   = sys.argv[1]
url      = sys.argv[2]
cur_path = sys.argv[3]
json_path = sys.argv[4] if len(sys.argv) > 4 else None

with open(cur_path, 'r') as f:
    data = json.load(f)

companies = data.get("companies", [])

# Load metadata from [TICKER].json if it exists
meta = {}
if json_path and os.path.exists(json_path):
    with open(json_path, 'r') as f:
        meta = json.load(f)
    print(f"Loaded metadata from {json_path}", file=sys.stderr)
else:
    print(f"No metadata file found, only updating analyseUrl", file=sys.stderr)

# Find and patch existing company, or append new
found = False
for c in companies:
    if c.get("ticker") == ticker:
        # Patch fields from meta (preserve events + chatUrl)
        for key, val in meta.items():
            if key not in ("events", "chatUrl"):
                c[key] = val
        c["analyseUrl"] = url
        found = True
        break

if not found:
    new_co = meta.copy() if meta else {}
    new_co["ticker"] = ticker
    new_co["analyseUrl"] = url
    companies.append(new_co)

data["companies"] = companies
print(json.dumps(data))
