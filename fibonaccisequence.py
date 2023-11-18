
def main(listtype:str):
    while True:
        print('\nYou can switch list modes: `--switch comma|newline` | Current mode: `comma`')
        terms = input("Input the number of terms: ")
        n1, n2 = 0, 1
        count = 0

        if terms.isnumeric():
            terms = int(terms)

            if terms <= 0:
                print("\nPlease input a positive integer that is greater than 0.")
                pass
            elif terms == 1:
                print("\nFibonacci sequence upto",terms,"term:")
                print(n1)
            else:
                seq = [0]
                print("\nFibonacci sequence upto",terms,"terms:")
                while count < terms:
                    nth = n1+n2
                    n1 = n2
                    n2 = nth
                    seq.append(n1)
                    count += 1
                
                print(listtype.join(str(e) for e in seq))

        else:
            if terms in ['--switch comma', '--switch c', '--switch ,']:
                listtype = ', '
                print("\nIt will now output the sequence using commas.")
                pass
            elif terms in ['--switch newline', '--switch n', '--switch nl']:
                listtype = '\n'
                print("\nIt will now output the sequence using new lines.")
                pass
            else:
                print("\nPlease input an integer.")
                pass


if __name__ == "__main__":
    print("Fibonacci Sequence Program by Len.icon\n")
    listtype = ', '
    main(listtype)


