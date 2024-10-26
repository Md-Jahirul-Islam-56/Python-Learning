import random

game = [ ['Draw','Win','Loss'],
        ['Loss','Draw','Win'],
        ['Win','Loss','Draw']
        ]

while(1):

    c=input("Press 1 to play the game or 2 to end the game:")

    if c=='1':

        choices = ['0', '1', '2']
        random_choice = random.choice(choices)

        user_input= int(input("Input 0 for Snake, 1 for Water and 2 for Gun:"))

        print("Computer Chose:",end="")
        print("Snake") if random_choice=='0' else print("Water") if random_choice=='1' else print("Gun") if random_choice=='2' else print(None)
        print(game[user_input][int(random_choice)])

    else:
        break