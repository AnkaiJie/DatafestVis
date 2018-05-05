import json

j = json.load(open("ExpRequiredByState.json", 'rb'))
cache = {}
for item in j:
    name = item['Name']
    if name not in cache:
        cache[name] = 0
    cache[name] += item["Mean"]
json.dump(cache, open("testData.json", 'wb'))
