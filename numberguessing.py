"""
Pick a random number from 1-100
When the user is incorrect, they give a hint such as 'the number is divisible to...', 'it's a multiple of...', 'it's odd/even'"
"""

import random
from time import sleep

def main():
    while True:
        answer = random.randint(1, 100)
        tries = 0
        hint: str

        print("I picked a number from 1-100.")

        while True:
            guess = input("Guess my number: ")

            if guess.isnumeric() and guess.isspace() == False:
                if int(guess) != answer:
                    tries += 1
                    print(f"\nWRONG! It's NOT {guess}")
                    
                    if (answer % 2) == 0 and (int(guess) % 2) != 0: hint = "The answer is an EVEN number."
                    elif (answer % 2) != 0 and (int(guess) % 2) == 0: hint = "The answer is an ODD number."
                    else:
                        if answer < int(guess): hint = f"The answer is LESS than {guess}."
                        else: hint = f"The answer is GREATER than {guess}." 
                    
                    print("Hint: ", hint ,"\n")
                    continue
                
                else:
                    print(f"\nCORRECT! The answer is {answer}!")
                    print(f"It took you {tries} tries until you got it right!\n")
                    replay = input("Wanna play again? [y/n]: ")

                    if replay.lower() == "y":
                        print("\nAlright! Let's play again!\n")
                        break
                    
                    else:
                        print("Okay, bye bye!\n")
                        exit()
            else:
                print("\nPlease input an INTEGER!\n")
                break
        
        continue

if __name__ == "__main__":
    print("Number Guessing Program by Len.icon\n")
    main()