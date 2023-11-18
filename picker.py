"""
Picker.
1. Get input
2. Add inputs in list
3. If you type command "--pick", randomly pick 1 thing from list
"""

from random import choice
from time import sleep

def mainphase(picker_list):
    while True:
        sleep(0.5)
        picker_input = input("Input something: ")

        if picker_input.split():
            if picker_input == "--pick":
                pickphase(picker_list)
            else:
                picker_list.append(f"{picker_input.capitalize()}\n")
                print("\nLIST:\n-", '- '.join(picker_list))
                mainphase(picker_list)
        else:
            pass

def pickphase(picker_list):
    while True:
        if len(picker_list) < 2:
            print("\nYou didn't give me much to decide on.\n")
            break
        else:
            print(f"\nPICKED: {choice(picker_list)}")
            sleep(0.2)
            print("You're welcome!")
            sleep(0.3)
            print("If you want me to repick, do '--repick'.\nIf you want me to pick from different choices, do '--restart'")
            sleep(0.3)
            endinput = input("\nWhat will it be, '--repick' or '--restart'? ")
            
            if endinput == "--repick":
                print("Okay then.")
                sleep(0.2)
                pickphase()
            
            elif endinput == "--restart":
                print("Restarting...\n")
                picker_list.clear()
                mainphase()
                

if __name__ == "__main__":
    print("Choice Picker by Len.icon\n")
    picker_list = []
    mainphase(picker_list)