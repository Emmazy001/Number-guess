import random


def number_guess():
    x=random.randint(1,100)
    i=0
    while True:
        try:
            guess=int(input("Guess the number: "))
            if 1>guess or guess>100:
                print("out of range")
                continue
            else:
                i = i + 1
            if guess==x:
                print("Correct")
                print('Number of attempts:',i)
                break
            elif guess<x:
                print("Higher")
            else:
                print("Lower")

        except ValueError:
            print("Wrong Input")

def play_game():
    while True:
        number_guess()
        while True:
            choice=input("play again? y/n: ")
            if choice == 'y':
                break
            elif choice == 'n':
                print("Goodbye")
                return
            else:
                print("Wrong Input")


play_game()






