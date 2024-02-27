import random as r


def play():
    user = input("""'R' for Rock
'P' for Paper
'S' for Scissors

Your Choice:""").lower()
    com = r.choice(['r', 'p', 's'])

    choices = {'r':0, 's':1, 'p':2}

    if user not in choices.keys():
        print("Enter valid choice!")
        exit()

    print(f'\nComputer chose: {com.upper()}\n')

    if (choices.get(user) - choices.get(com)) % 3 == 2:
        print('You Won!')
    elif (choices.get(user) - choices.get(com)) % 3 == 1:
        print('You Lost!')
    else:
        print("It's a Tie!")


play()

#another dummy commit