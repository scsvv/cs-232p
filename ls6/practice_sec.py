# -> 
items = [1, 2, 1, 2, 3, 4, 5, 1, 6, 5, 7]
copy_items = items.copy()

for item in items: 
    c = items.count(item)
    for i in range(c - 1):
        items.remove(item)

print(items)
print(copy_items) 

new_item = set(copy_items)
new_item.add(1)
print(new_item)

