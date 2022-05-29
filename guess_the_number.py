import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while (random_number != guess):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if random_number < guess:
            print("Your number is too high!")
        elif random_number > guess:
            print("Your number is too low!")
    print("You guess the number correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print("Computer guess the right number")

if __name__=="__main__":
    option = int(input("If you want to guess, then press 1:\nIf you want computer to guess, then press 2:\n"))
    if option == 1:
        guess(1000)
    elif option == 2:
        computer_guess(1000)
    else:
        print("you have selected the wrong option!!")