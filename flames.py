def main():
    name = input("Input Your Name: ")
    if (not name.strip()): quit()

    cname = input("Input Your Crush's Name: ")
    if (not cname.strip()): quit()

    count = countName(name.lower().replace(" ",""), cname.lower().replace(" ",""))
    flames(count)

    main()


def countName(name, cname):
    a = ''.join(c for c in name if c not in cname)
    b = ''.join(c for c in cname if c not in name)

    return (len(a) + len(b))

def flames(num):
    while (num > 6):
        num -= 6
    
    match(num):
        case 1: print("Result: FRIENDS\n")
        case 2: print("Result: LOVERS\n")
        case 3: print("Result: ACQUAINTANCES\n")
        case 4: print("Result: MARRIED\n")
        case 5: print("Result: ENEMIES\n")
        case 6: print("Result: SEX PARTNERS\n")
        case _: print("Result: CLONES\n")
            


if __name__ == "__main__":
    print("FLAMES Program by Len.icon\n")
    main()
    