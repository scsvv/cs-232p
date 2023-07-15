# Boolean -> !

""" 
Операции сравнения

* Операции сравнения для численных типов переменных: 
    >   |   <      больше, меньше
    >=  |   <=     больше либо равно, меньше либо равно

* Операции, которые работают с числами и со строками (булианы, списки, ссылки):

    ==          проверка на равенство 
    !=          проверка на не равенство 
"""
# a, b, c = 10, 10, 9
# d = c
# print(f'a > b = {a} > {b}: {a > b}')
# print(f'a >= b = {a} >= {b}: {a >= b}')
# print(f'a > c = {a} > {c}: {a > c}')
# print(f'a == b => {a} == {b}: {a == b}')
# print(f'a == c => {a} == {c}: {a == c}')

# s1, s2, s3 = 'a', 'b', 'a'
# print(s1 == s2)
# print(s1 == s3)

# mock_password = 'qwerty12345'
# password = input('Enter your password: ')
# print(mock_password == password)

"""
Операции над самими булианами. 
- and 
- or 
- not
"""
a, b, c = True, False, True
print(a or b)
print(a or c)
print(not(a))