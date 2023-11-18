from json import load
from os import path
from random import randint

def abm(abvOn):
    abvmode = input("[0] No Abbreviations\n[1] Can Use Abbreviations\nInput Abv. Mode #: ").strip()

    if (not abvmode.strip()) or (not int(abvmode)) or (abvmode != '0') or (abvmode != '1'):
        abm()
    else:
        abvOn = bool(abvmode)
    
    return

def anm(codonOn, aminoOn):
    anmode = input("\n[0] Both\n[1] Codons Only\n[2] Amino Acids Only\nInput Test Mode #: ").strip()

    if (not anmode.strip()) or (not int(anmode)) or (anmode != '0') or (anmode != '1')or (anmode != '2'):
        abm()
    else:
        y = int(anmode)

        match(y):
            case 0:
                codonOn = True
                aminoOn = True
            case 1:
                codonOn = True
                aminoOn = False
            case 2:
                codonOn = False
                aminoOn = True
    
    return

def mode():
    #ask for mode, with abv, or no abv
    y = 0
    abvOn = False
    codonOn = True
    aminoOn = True

    abm(abvOn)

    anm(codonOn, aminoOn)
    
    
    return [abvOn, codonOn, aminoOn]
    


def main(score:int, aminoAnswered:list, codonAnswered:list, abvOn:bool, codonOn:bool, aminoOn:bool):
    file_path = path.abspath(__file__) # full path of your script
    dir_path = path.dirname(file_path) # full path of the directory of your script
    f = open(path.join(dir_path, 'quiz.json'),)
    quiz = load(f)

    #loop through quiz array
    #pick either codon, amino
    qSet = randint(0, len(quiz)-1)

    qTypes = []

    if codonOn: qTypes.append("codon")
    if aminoOn: qTypes.append("amino")

    if qTypes!=[]: qType = qTypes[randint(0, 1)]

    if qType == "codon":
        codonQuiz(quiz, qSet, score, aminoAnswered, abvOn)
    else:
        aminoQuiz(quiz, qSet, False, score, aminoAnswered)

    # print(quiz[qSet].get(qTypes[qType]))

def codonQuiz (quiz, num:int, score:int, codonAnswered:list, abvOn: bool):
    getQuiz = quiz[num].get("codon")
    codon = getQuiz[randint(0, len(getQuiz)-1)]
    amino = quiz[num].get("amino")
    abv = ""

    if abvOn == True:
        abv = quiz[num].get("abv")

    while (codon.upper() in codonAnswered):
        codon = getQuiz[randint(0, len(getQuiz)-1)]
    else:
        answer = input("The codon, " + codon + ", translates to what amino acid? ")
        codonAnswered.append(codon)

    if (answer == amino) or (abvOn == True and answer == abv):
        print("Correct!\n")
        score = score + 1
        main(score, codonAnswered)
    else:
        if (answer == "quit"): quit()
        print("Wrong! It's " + amino.capitalize() + ".\n")
        print("SCORE: " + str(score) + "\n")
        quit()


def aminoQuiz (quiz, num:int, repeated:bool, score:int, aminoAnswered:list):
    saveNum = num
    amino = quiz[num].get("amino")
    codons = quiz[num].get("codon")

    if repeated:
        answer = input("You already aminoAnswered that, what else? ")    
    else:
        answer = input("The amino acid, " + amino.capitalize() + ", translates to what codon? Give one: ")

    #have a list of aminoAnswered codons, to avoid redundancy
    #check if all codons of an amino acid are all inside the list
    #remove the codons, to start anew

    if answer.upper() in codons:
        if set(codons).issubset(aminoAnswered):
            aminoAnswered = [i for i in aminoAnswered if i not in codons]

        if answer.upper() in aminoAnswered:
            aminoQuiz(quiz, num, True, score, aminoAnswered)
            
        else:
            aminoAnswered.append(answer.upper())
            print("Correct!\n")
            score = score + 1
            main(score, aminoAnswered)
    else:
        if (answer == "quit"): quit()
        a = ', '.join(codons)
        b = a.rsplit(', ', 1)
        print("Wrong! It's " + " or ".join(b) + ".\n")
        print("SCORE: " + str(score) + "\n")
        quit()
            


if __name__ == '__main__':
    print("Codon & Amino Quizer by Len.icon\nFor Iana ♥")
    score = 0
    aminoAnswered = []
    codonAnswered = []
    mod = mode()
    main(score, aminoAnswered, codonAnswered, mod[0], mod[1], mod[2])

