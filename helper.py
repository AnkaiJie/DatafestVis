import json

j = json.load(open("EducationByState.json", 'rb'))
cache = {}
for item in j:
    name = item['Name']
    if name not in cache:
        cache[name] = 0
    cache[name] += item["Number"]
json.dump(cache, open("testData.json", 'wb'))
