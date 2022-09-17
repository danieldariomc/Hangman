import os
import random


def Menu():
    with open("./Menu.txt", "r") as menu:
        menuContent = menu.read()
        print(menuContent)


def HowToPlay():
    with open("./HowToPlay.txt", "r") as HowToPlay:
        HowToPlayContent = HowToPlay.read()
        print(HowToPlayContent)
        returnMenu = input("Type \"menu\" to come back to the principal menu: ")
        if returnMenu == "menu":
            Run()


def Wordlist():
    wordList = []
    with open("./Words.txt", "r", encoding="utf-8") as Words:
        for word in Words:
            word = word.replace("\n", "")
            wordList.append(word)
    return wordList


def WordGenerator():
    wordList = Wordlist()
    randomIndex = random.randint(0, len(wordList))          
    guessWord = wordList[randomIndex]
    return guessWord


def Congratulation():
     with open("./Congratulation.txt", "r") as Congratulation:
        CongratulationContent = Congratulation.read()
        print(CongratulationContent)
        returnMenu = input("Type \"menu\" to come back to the principal menu: ")
        if returnMenu == "menu":
            Run()


def Images(counter):
    if counter == 0:
        with open("./Images/Image_1.txt", "r") as Images:
            print(Images.read())
    elif counter == 1:
        with open("./Images/Image_2.txt", "r") as Images:
            print(Images.read())
    elif counter == 2:
        with open("./Images/Image_3.txt", "r") as Images:
            print(Images.read())
    elif counter == 3:
        with open("./Images/Image_4.txt", "r") as Images:
            print(Images.read())
    elif counter == 4:
        with open("./Images/Image_5.txt", "r") as Images:
            print(Images.read())
    elif counter == 5:
        with open("./Images/Image_6.txt", "r") as Images:
            print(Images.read())
    elif counter == 6:
        with open("./Images/Image_7.txt", "r") as Images:
            print(Images.read())
    elif counter == 7:
        with open("./Images/Image_8.txt", "r") as Images:
            print(Images.read())


def startGame():
    print("\n")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print("Try to guess the next word: ")
    guessWord = WordGenerator()                        
    underscoreWord = len(guessWord) * "_"
    counter = 0 
    while guessWord != underscoreWord:
        printWord = underscoreWord
        printWord = " ".join(list(printWord))
        print(printWord)
        print("\n")
        Images(counter)
        letter = input("Insert a letter: ")
        letter = letter.lower()
        if counter <= 6:
            if letter in guessWord:
                underscoreWord = list(underscoreWord)
                for index, element in enumerate(guessWord):
                    if letter == element:
                        underscoreWord[index] = element
                underscoreWord = "".join(underscoreWord)
            else:
                counter = counter + 1
        else:
            os.system("cls")
            print("Your word was:",guessWord)
            with open("./Images/Image_9.txt", "r") as GameOver:
                print(GameOver.read())
            returnMenu = input("Type \"menu\" to come back to the principal menu: ")
            if returnMenu == "menu":
                Run()
        os.system("cls")
    print("You won! The word was:", guessWord.upper())
    Congratulation()


def AddWord():
    os.system("cls")
    newWord = input("Insert a new word to add to the game: ")
    newWord = newWord.lower()
    worlList = Wordlist()
    if newWord in worlList:
        print("The word", newWord,"is already in the game")
    else: 
        print("The world", newWord,"was added to the game")
        with open("./Words.txt", "a") as addNewWord:
            addNewWord.write("\n")
            addNewWord.write(newWord)
            addNewWord.close()
    returnMenu = input("Type \"menu\" to come back to the principal menu: ")
    if returnMenu == "menu":
        Run()


def GoodBye():
    with open("./Goodbye.txt", "r") as Goodbye:
        GoodbyeContent = Goodbye.read()
        print(GoodbyeContent)
        exit()
        

def Run():
    os.system("cls")
    Menu()
    index = int(input("Insert a number related with the option: "))
    if index == 1:
        HowToPlay()
    elif index == 2:
        startGame()
    elif index == 3:
        AddWord()
    elif index == 4:
        GoodBye()


if __name__ == "__main__":
    Run()