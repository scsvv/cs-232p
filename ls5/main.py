from random import randint
score = 0
actions = ("+", "-", "*")

for i in range(0, 5, 1):
    action, a, b = randint(0, 2), randint(0, 100), randint(0, 100)
    state = False

    match action:
        case 0:
            question = a + b
        case 1:
            question = a - b
        case 2:
            question = a * b
        case _ :
            print("Oops")

    action = actions[action]
    
    trying = 0
    while not(state):  
        answer = input(f'{a}{action}{b} = ')
        try: 
            answer = int(answer)
        except:
            print("Type number, not format one / twenty one only 1 / 21")

        if answer ==  question: 
            score += 5
            print(f"Yep, u have {score}")
            state = True
        else: 
            score += - 1 + (-trying*1) 
            print(f"Lets try again, u lose {-1 + -(trying*1)} points, your score is {score}")
            trying += 1

print(score)
