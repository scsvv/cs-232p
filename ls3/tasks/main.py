# year = input("Enter year: ")
# try:
#     year = int(year)
# except: 
#     print('Err: invalid data')
#     exit()
# print(f'{year} leap year: {(year % 4) == 0}')

# number = input("Enter your number: ")
# try:
#     number = int(number)
#     print(f'Is more than 0: {number > 0}')
# except:
#     print('Error: Invalid Data')
#     exit()

# Odd Even -> 1 2 
number = input("Enter number: ")
try: 
    number = int(number)
    print(f'Is over number even: {(number % 2) == 0}')
except: 
    print('it\'s not a number')