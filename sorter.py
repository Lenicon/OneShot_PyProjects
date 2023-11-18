from time import sleep
from random import shuffle

def mainphase():
    global sortlist
    sortlist = []
    global sorttype
    global listtype

    while True:
        e = input("\nAdd element or --sort: ")

        if e.split():
            if e.lower() == "--sort":
                if len(sortlist) < 2:
                    print("\nThere should be at least 2 elements!")
                else:
                    print("\nList: ", sortlist)
                    sortphase()
            
            else:
                sortlist.append(e)
                print("\nList: ",sortlist)
            
            pass
        else:
            pass

def sortphase():
    while True:
        print("\nSort Types: az, za, baz, bza, shortlong, longshort, shuffle, dont | (Default = az)")
        print("List Types: comma, bullet, dash, number, newline, dont | (Default = comma)")
        print("(You could `--reset` or `--quit` if you want to.)")
        st = input("\nInput `[sort_type|0] [list_type|0]` or Nothing for default: ")

        if st.split():
            if st.lower() == '--reset':
                print('Resetting...')
                mainphase()
            elif st.lower() == '--quit':
                print("Okay, byebye!\n")
                exit()
            else:
                spst = st.lower().split()
                
                sorttype = spst[0]

                if sorttype in ['0', 'az']: sortlist.sort()
                elif sorttype == 'baz': sortlist.sort(key=lambda x:x[-1])
                elif sorttype == 'za': sortlist.sort(reverse=True)
                elif sorttype == 'bza': sortlist.sort(key=lambda x:x[-1], reverse=True)
                elif sorttype in ['shortlong', 'sl', 'len']: sortlist.sort(key=len)
                elif sorttype in ['longshort', 'ls', 'revlen']: sortlist.sort(key=len, reverse=True)
                elif sorttype in ['shuffle', 'random', 's', 'r', 'shuf','rand']: shuffle(sortlist)
                elif sorttype == 'dont': pass
                else: sortlist.sort()

                if len(spst) == 2:
                    listtype = spst[1]

                    i = 0

                    if listtype in ['0', 'comma']: print("\nList: ", ', '.join(sortlist))
                    elif listtype in ['newline', 'line', 'new']:
                        print("\nList:")
                        print('\n'.join(sortlist))
                    elif listtype == 'dont': print(sortlist)
                    elif listtype in ['bullet', 'b', 'bul', 'o']:
                        print("\nList:")
                        for e in sortlist:
                            print(f"• {e}")

                    elif listtype in ['dash', '-', 'd']:
                        print("\nList:")
                        for e in sortlist:
                            print(f"- {e}")

                    elif listtype in ['number', 'ordered', 'numbered', 'ordered', 'n']:
                        print("\nList:")
                        for e in sortlist:
                            i += 1
                            print(f"{str(i)}. {e}")
                    
                    else: print("\nList:", ', '.join(sortlist))


                else:
                    print(', '.join(sortlist))
                
                sleep(1)
                sortphase()

        else:
            print(', '.join(sortlist.sort()))
            
            sleep(1)
            sortphase()

            

def restart():
    sleep(0.5)
    ri = input("\nWanna `reset`, `resort`, or `quit`? [reset|resort|quit]: ")

    if ri.lower() == 'reset':
        print('Resetting...')
        mainphase()
    elif ri.lower() == 'resort':
        print('Heading to Sorting Phase...')
        sortphase()
    else:
        print("Okay, byebye!\n")
        exit()

# Start Main Phase

if __name__ == "__main__":
    print("Sorter Program by Len.icon\n")
    mainphase()