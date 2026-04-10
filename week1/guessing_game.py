# Date: Apr. 9, 2026
# Author: Paul Han
# A simple number guessing game

import random

def main():
    num = random.randint(0,100)

    print("Welcome to the number guessing game! \n \
            You have 8 chances to guess the number. \n \
            The number is between 0 and 100 (inclusive). \n \
            Good luck!")

    for i in range (1,9):
        x = int(input(f"Guess #{i}: "))
        if x == num:
            print(f"Good job! You got it!")
            return
        else:
            if i == 8:
                print(f"Noooo, the number was {num} :(")
                return
            if x > num:
                print(f"Try again, the number is lower!")
            if x < num:
                print(f"Try again, the number is higher!")

if __name__ == "__main__":
    main()
