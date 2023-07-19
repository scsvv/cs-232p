# work flow if 
"""
mock_password = 'qwerty12345'
password = input('Enter your password: ')

if mock_password == password:
    print("Welcome in system")
else: 
    print("access dined")

if 4 == 4:
    print(4)


Task 1: 
Пользователь вводит номер дня недели. Выведите строку 'Выходные', если введенное число равно 6 или 7. В случае, если число лежит в диапазоне от 1 до 5 включительно, выведите строку 'Будни'


days = ["Monday", "Tuesday", "Wendsday", "Thrusday", "Friday", "Saturday", "Sunday"]
day = input("Enter day`s number: ")

try:
    day = int(day)
except: 
    print("Error 1: Not correct data type")
    exit()

if day > 0 and day < 6:
    print(f"{days[day - 1]} is work day")
elif day == 6 or day == 7:
    print(f"{days[day - 1]} is holiday")
else: 
    print("Error 2: Not work interval")

import datetime
today = datetime.datetime.now()
day = today.strftime("%w")

try:
    day = int(day)
except: 
    print("Error 1: Not correct data type")
    exit()

if day > 0 and day < 6:
    print(f"Today { today.strftime('%A') } is work day")
elif day == 6 or day == 7:
    print(f"Today { today.strftime('%A') } is holiday")
else: 
    print("Error 2: Not work interval")



from random import randint 
x = randint(1, 10)
print(x)
guess = input("Enter number: ")
if int(guess) == x:
    print("You Win")

b = 10 

if b > 0: 
    print("B")
elif b > 5: 
    print("Bb")
elif b > 7: 
    print("Bbb")


"""

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a + b >= c and a + c >= b and b + c >= a:
    print("It's a trangle")
else:
    print("Oops.. Somethigs Is Going Bad")
