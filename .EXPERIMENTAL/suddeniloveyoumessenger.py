import pyautogui
from time import sleep
import subprocess
import random

#(616, 347-485), (370, 852)or(355,372), (901, 978),
dumbinputs = [
    "Hello, this is Susan Waikiki your sugar moommy. I will send you $1000 if you send me your bank information.",
    "I need help my friend. Please send me 20pesos so that I can save my daughter. I just need 20 pesos please. My gcash is 696969420. ill pay u back pls send.",
    "If they have L and H in their name, gwapo yan. so be careful"
]

where=input("1 or 2?")

if where=="1":
    sleep(5)
    command = f"cmd /c start msedge https://www.messenger.com/ --new-window"
    sleep(0.1)
    subprocess.Popen(command, shell=True)
    sleep(15)
    pyautogui.moveTo(616, 347)
    pyautogui.dragTo(616, 347, button="left")
    pyautogui.dragTo(616, 485, button="left", duration=1)
    sleep(0.2)
    pyautogui.leftClick(370, 852)
    sleep(10)
    pyautogui.leftClick(901, 978)
    sleep(0.3)
    pyautogui.typewrite(random.choice(dumbinputs), interval=0.25)
    sleep(5)
    pyautogui.press('enter')
else:
    sleep(5)
    command = f"cmd /c start msedge https://www.messenger.com/ --new-window"
    sleep(0.1)
    subprocess.Popen(command, shell=True)
    sleep(19)
    pyautogui.leftClick(901, 978)
    sleep(0.3)
    pyautogui.typewrite(random.choice(dumbinputs), interval=0.1)
    """ pyautogui.press('enter')
    pyautogui.typewrite("I hope this is not an important gc.", interval=0.1)
    pyautogui.press('enter')
    pyautogui.typewrite("because im testing out a program that takes control of your computer and sends dumb responses to people on messenger.", interval=0.1)
    pyautogui.press('enter')
    pyautogui.typewrite("This is an automated response btw.", interval=0.1) """
    pyautogui.press('enter')
    