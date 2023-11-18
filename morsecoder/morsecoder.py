from json import load, loads
from os import path

def main(codetype):
    file_path = path.abspath(__file__)
    dir_path = path.dirname(file_path)
    f = open(path.join(dir_path, 'morses.json'))
    mc = load(f)

    if codetype == 0:
        s = input("\nInput Text (or --switch): ").upper()
        if s == '--SWITCH':
            main(1)
        elif s == '`':
            quit()
        else: encode(s, mc)
    else:
        print("\n*Add space for every code\n*Add '/' if you want space between text")
        s = input("\nInput Morse Code (or --switch): ")
        if s == '--switch':
            main(0)
        elif s == '`':
            quit()
        else: decode(s, mc)

def encode(inputStr:str, morseDict):
    characters = list(inputStr)
    # print(characters)
    test = '{"A":"lol"}'
    filteredChars = [char for char in characters if char in morseDict or char == " "]
    filteredStr = ''.join(filteredChars)
    # encoded = ' '.join([morseDict.get(char.upper(), char) for char in filteredStr])
    encoded = ' '.join([morseDict[char.upper()] if char.upper() in morseDict else char for char in filteredStr.replace(" ", "//")])
    print("\nTEXT: "+ filteredStr)
    print("RESULT: "+ encoded.replace("/ /", "//") + " ///")
    main(0)

def decode(inputStr:str, morseDict):
    characters = inputStr.split()
    rMorseDict = {v: k for k, v in morseDict.items()}
    decoded_characters = [rMorseDict.get(code, characters) for code in characters]
    decoded = ''.join(decoded_characters)
    print("\nCODE: "+ inputStr.replace(" ", " // "))
    print("RESULT: "+ decoded)
    main(1)
    

if __name__ == "__main__":
    print("Morse Code Encoder/Decoder by Len.icon")
    main(0)