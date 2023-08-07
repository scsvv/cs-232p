products = dict()

K = input("type K: ")
try:
    K = int(K)
except ValueError:
    K = 0

for i in range(K):
    data = input("type data in (name, count): ")
    data = data.split(',')
    try:
        value = int(data[1])
    except:
        value = None

    products.setdefault(data[0], value)

print(products)


# friends = [
#     dict(name="Ivan", age=18),
#     dict(name="Egor", age=17),
#     dict(name="Genadiy", age=23),
#     dict(name="Kirill", age=16),
#     dict(name="Alex", age=18),
#     dict(name="Gleb", age=22),
#     dict(name="Vasiliy", age=24),
# ]
# print(friends)

# min_age = [1000, '']
# max_length = ''
# for friend in friends:
#     if friend.get('age') < min_age[0]:
#         min_age[0], min_age[1] = friend.get('age'), friend.get('name')
#     if len(friend.get('name')) > len(max_length):
#         max_length = friend.get('name')

# print(max_length, min_age)
