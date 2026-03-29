import json, sys

ticker = sys.argv[1]
url = sys.argv[2]
data = json.loads(sys.argv[3])

companies = data.get("companies", [])
found = False
for c in companies:
    if c.get("ticker") == ticker:
        c["analyseUrl"] = url
        found = True
        break
if not found:
    companies.append({"ticker": ticker, "analyseUrl": url})

data["companies"] = companies
print(json.dumps(data))
