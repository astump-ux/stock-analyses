import json, sys, os

ticker    = sys.argv[1]
json_file = sys.argv[2]
index_file = sys.argv[3]

with open(index_file, 'r', encoding='utf-8') as f:
    index = json.load(f)

# Load metadata patch if exists
meta = {}
if os.path.exists(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    print(f"Loaded {json_file}", file=sys.stderr)
else:
    print(f"No {json_file} found", file=sys.stderr)

companies = index.get("companies", [])
found = False
for c in companies:
    if c.get("ticker") == ticker:
        # Patch all fields from meta except events/chatUrl (preserve)
        for key, val in meta.items():
            if key not in ("events", "chatUrl"):
                c[key] = val
        found = True
        break

if not found and meta:
    companies.append(meta)

index["companies"] = companies
index["updatedAt"] = __import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')
print(json.dumps(index, ensure_ascii=False))
