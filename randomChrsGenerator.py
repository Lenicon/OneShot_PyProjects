from random import choice, shuffle

def randTxt(num):
    clist = []
    for _ in range(num):
        ch = choice("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890:,_-=+[]/!?~")
        clist.append(ch)
    
    shuffle(clist)
    res = "".join(clist) + " - "
    print(res)

if __name__ == "__main__":
    print("Random Character(s) Generator by Len.icon\n")
    num = int(input("Input # of Characters: "))
    given = int(input("Input # of Given: "))
    
    for _ in range(given):
        randTxt(num)