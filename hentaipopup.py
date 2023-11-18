"""
gather all hentai links and make it into a list
randomly get one of those links
turn it into a popup...
"""

import random
from time import sleep
from subprocess import Popen

popups = ['https://www.nutaku.net/home/','https://www.nutaku.net/games/project-qt/', 'https://www.nutaku.net/games/lusty-odyssey/', 'https://www.nutaku.com/', 'https://nhentai.net/g/454696/18/', 'https://www.nutaku.com/games/camgirls-inc-online/', 'https://nhentai.net/g/454699/1/']

def main():
    while True:
        sleep(random.randint(10, 20))
        selectedone = random.choice(popups)
        command = f"cmd /c start msedge {selectedone} --new-window"
        sleep(0.3)
        Popen(command, shell=True)

if __name__ == "__main__":
    print("Hentai Popup Program by Len.icon\n")
    main()