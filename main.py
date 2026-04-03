import random


def number_guess():
    x=random.randint(1,100)
    i=0
    while True:
        try:
            guess=int(input("Guess the number: "))
            if guess>100 or 1>guess:
                print("out of range")
            elif guess==x:
                print("Correct")
                print('Number of attempts:',i)
                break
            elif guess<x:
                print("Higher")
            elif guess>x:
                print("Lower")
            else:
                print("Wrong")
        except ValueError:
            print("Wrong Input")
        i=i+1

number_guess()