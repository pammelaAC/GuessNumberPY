import random


def number(x):
    random_number = random.randint(1,x)
    number = 0

    while number != random_number:    
        number = int(input(f'Guess a number between 1 and {x}: '))        
        if number > random_number:
            print("Sorry, guess again. Too high.") 
            print()
        elif number < random_number:
            print("Sorry, guess again. Too low.") 
            print()

    print(f'Congrats! You have guessed the number {number} corrrectly!')
    
number(10)