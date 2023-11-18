from time import sleep
from os import path, listdir, remove, getenv
import pyuac


def main():
    timeset = input("Clean every _ minutes: ")

    if timeset.isnumeric() and timeset.split():

        while True:
            clean()
            sleep(timeset * 10000)

    else:
        main()

def clean():
    homedir = path.expanduser('~')
    cleanlist = ['C:\Windows\Temp', path.join(getenv('LOCALAPPDATA'),'Temp'), path.join(homedir, 'Recent')]
    m = []
    for i in cleanlist:
        for j in listdir(i):
            m.append(m)
    print(m)


if __name__ == '__main__':
   if not pyuac.isUserAdmin():
       print('Relaunching as ADMIN...')
       pyuac.runAsAdmin()
   else:
       main()
    