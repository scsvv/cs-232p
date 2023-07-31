# N -> func

# declare function  
from random import randint
def password_generation(quantity, upper=True):
    mock_password ='lYzkUs#uOdaGhigIT/KPjeboqncfpvWm&?txwyrQ@'
    password = ''
    for i in range(quantity):
        _u = randint(1, 10)
        _s = mock_password[randint(0, 30)]
        if _u > 8 and upper:
            _s = _s.upper()
        else:
            _s = _s.lower()
        password += _s
    return password

name = input("Type password name: ")
p1 = password_generation(12)

with open(f"{name}.txt", "w") as file1:
    file1.write(f"{p1}")
