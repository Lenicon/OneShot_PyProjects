def xinp():
    global x
    x = input("\nInput x integer: ")

    if x.isnumeric() and x.isspace() == False:
        yinp()
    else:
        print("\nPlease input an INTEGER!")
        xinp()

def yinp():
    global y
    y = input("\nInput y integer: ")
    
    if y.isnumeric() and y.isspace() == False:
        check()
    else:
        print("\nPlease input an INTEGER!")
        yinp()

def check():
    global lower
    global upper
    newx = int(x)
    newy = int(y)

    if newx > newy:
        upper = newx
        lower = newy
    elif newx < newy:
        upper = newy
        lower = newx
    else:
        print("\nThe two integers MUST NOT BE EQUAL!")
        print("Restarting...\n")
        print("\nThis will print prime numbers between x and y integers.")
        xinp()

    print(f"\nThe prime numbers between {lower} and {upper} are:")

    plist=[]
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) != 0 and num not in plist:
                    plist.append(num)
                else:
                    break
    
    print(', '.join(str(e) for e in plist)+"\n")
    restart = input("Restart? [y/n]: ")
    if restart.lower() == "y":
        print("Restarting...\n")
        print("\nThis will print prime numbers between x and y integers.")
        xinp()
    else:
        print("Alright, byebye!\n")
        exit()


if __name__ == "__main__":
    print("Prime Numberer by Len.icon\n")
    xinp()


            