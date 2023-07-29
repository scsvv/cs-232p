load = [{"name": "L"}, {"name": "D"}, {"name": "I"}] # to load 
loaded = [{"name": "U"}, {"name": "S"}, {"name": "I"}] # loaded

b_name = set()
for doc in loaded:
    b_name.add(doc["name"])

for doc in load:
    if doc["name"] in b_name:
        continue
    loaded.append(doc)

print(loaded[0].items())

