"""
Problem 
25 -> 2 + 5 -> ?
10 - 99 right 

+ - / // %  * ** 
X - ? 
"""
number = input('Enter your number: ')
try:
    number = int(number)
except:
    print("Error 1, not valid data \nExit 0")
    exit()
left, right = number // 10, number % 10
print(f'{left} + {right} = {left + right}')

x, y = 10, 0
# try: 
#     x / y
# except:
#     print("Error")