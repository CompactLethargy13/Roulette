__version__ = "1.2.5" #build 10000
'''
====================================================================================================================================================================================================
IMPORTANT!!!!!!!! MAKE CHECK FOR GAMEMODE
how to use ansi codes:
print("\033[1;{ANSI_CODE} texts texts")
include choice of:
high or low (done)
odd or even (done)
or range of number (done)
add about and help page (doing)
add most if not all inside bets https://en.wikipedia.org/wiki/Roulette
try best as i can to add outside bets
====================================================================================================================================================================================================
'''
from time import sleep
import requests
import os
import urllib.request
import numbers
from turtle import clear
import random
import sys
import logging
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(filename = 'log.txt',level=logging.INFO)
logging.basicConfig(filename = 'log.txt',level = logging.ERROR)
#===================================================================================================================================================================================================
#init
logging.info("game started")
blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
firsts = [1,4,7,10,13,6,19,22,25,28,31,34]
seconds = [2,5,8,11,14,17,20,23,26,29,32,35]
thirds = [3,6,9,12,15,18,21,27,30,33,36]
usrCheck = True
gameMode = ''
betIncrease = 0
redOrBlack = None
userCheck = "n"
whichZero = ''
logging.info("initialized")
logging.info("checking version...")
#===================================================================================================================================================================================================
#def
def clearscr():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system('cls')
    else:
        print("Unknown Error: SystemUndefined\nProgram quit with exit code 4")
def checkOdd(num):
    if (num%2) == 0:
        return False
    else:
        return True
def checkLow(num):
    if num in range(1,20):
        return 4
    elif num in range(20,37):
        return 5
def checkRange3(num):
    if num in range(1,13):
        return 1
    elif num in range(13,25):
        return 2
    elif num in range(25,36):
        return 3
def checkUserRange(start,end,num):
    if num in range(start,end):
        return True
    else:
        return False
def checkRed(usrChoice,num,reds):
    for i in reds:
        if usrChoice == i:
            usrChoice = True
            break
        elif usrChoice != i:
            usrChoice = False
    for i in reds:
        if num == i:
            numIsRed = True
            break
        elif num != i:
            numIsRed = False
    if usrChoice == numIsRed:
        return True
    elif usrChoice != numIsRed:
        return False
#self update
def checkUpdates(__version__):
    print("Loading...")
    try:
        sleep(2)
        response = requests.get('https://raw.githubusercontent.com/CompactLethargy13/Roulette/main/version.txt')
        data = response.text
        data = data.translate({ ord("."): None })
        __GameVersion = __version__.translate({ ord("."): None })
        if int(data) > int(__GameVersion):
            print('Software Update Available!')
            print("Update!",version," needs to update to version ",data)
            while True:
                toUpdate = input("Do you want to update now? If no, this will be updated next time.(y/n):").lower()
                if toUpdate == "y" or toUpdate == "n":
                    break
                else:
                    continue
            if toUpdate == "y":
                fileCurrent = open(str(__file__), "r+")
                currentPath = __file__
                url = "https://raw.githubusercontent.com/CompactLethargy13/Roulette/main/rouletteSingleFile.py"
                newfilepath, headers = urllib.request.urlretrieve(url, filename = currentPath)
                newFile = open(str(newfilepath),"r+")
                list = fileCurrent.readlines()
                listToReplace = newFile.readlines()
                c = 0
                for i in list:
                    for j in listToReplace:
                        Replacement = i.replace(i,j)
                        replace = Replacement
                    c += 1
                fileCurrent.truncate(0)
                fileCurrent.writelines(replace)
                fileCurrent.close()
                print("Updated to "+data)
            else:
                pass
    except Exception as e:
        sleep(2)
        print('Software Update, Unable to Check for Update, Error:' + str(e))
        input("ENTER to continue")
    os.system("cls")
    os.system("clear")
def plannedChanges():
    print("No planned changes currently")
    input("ENTER to exit ")
class others:
    def aboutPage():
        pass
    def helpPage(question):
        if help == '?':
            quitOrNot = 'n'
            whichPage = -1
            while quitOrNot == 'n':
                whichPage = input("Choose which page you want to go:\n1: Betting multiplier\n2: Planned changes\n'q' to quit\nInput here: (1/2) ")
                while whichPage != '1' and whichPage != '2' and whichPage != 'q':
                    #os.system('cls')
                    #os.system('clear')
                    if whichPage != 'repeat':
                        print("Please input 1 or 2")
                    whichPage = input("Choose which page you want to go:\n1: Betting multiplier\n2: Planned changes\n'q' to quit\nInput here: (1/2) ")
                if whichPage == '1':
                    #os.system('cls')
                    #os.system('clear')
                    print("Betting on even or odd, or red or black    |   1: 1 return")
                    print("Betting on low or high range               |   1: 2 return")
                    print("Betting on a user-specified range          |   1: 3 return")
                    print("Betting on 0 or 00                         |   1:38 return")
                    whichPage = 'repeat'
                    input("ENTER to exit ")
                    clearscr()
                elif whichPage == '2':
                    plannedChanges()
                elif whichPage == 'q':
                    clearscr()
                    input("\033[1;37m  ______ _   _ _______ ______ _____    _              _             _   \n |  ____| \\ | |__   __|  ____|  __ \\  | |            | |           | |  \n | |__  |  \\| |  | |  | |__  | |__) | | |_ ___    ___| |_ __ _ _ __| |_ \n |  __| | . ` |  | |  |  __| |  _  /  | __/ _ \\  / __| __/ _` | '__| __|\n | |____| |\\  |  | |  | |____| | \\ \\  | || (_) | \\__ | || (_| | |  | |_ \n |______|_| \\_|  |_|  |______|_|  \\_\\  \\__\\___/  |___/\\__\\__,_|_|   \\__|")
                    break
#game starts

#auto-update is disabled here for obvious reasons
#checkUpdates(__version__)

logging.info("checking version done")
#enter to start
os.system("cls")
os.system("clear")
help = input("\033[1;37m  ______ _   _ _______ ______ _____    _              _             _   \n |  ____| \\ | |__   __|  ____|  __ \\  | |            | |           | |  \n | |__  |  \\| |  | |  | |__  | |__) | | |_ ___    ___| |_ __ _ _ __| |_ \n |  __| | . ` |  | |  |  __| |  _  /  | __/ _ \\  / __| __/ _` | '__| __|\n | |____| |\\  |  | |  | |____| | \\ \\  | || (_) | \\__ | || (_| | |  | |_ \n |______|_| \\_|  |_|  |______|_|  \\_\\  \\__\\___/  |___/\\__\\__,_|_|   \\__|\nQuestion mark (?) for help page: ")
others.helpPage(help)
clearscr()
#welcome text
print("\033[1;31m __          __  _                            _                          _      _   _         _   _   _  \n \\ \\        / / | |                          | |                        | |    | | | |       | | | | | |\n  \\ \\  /\\  / ___| | ___ ___  _ __ ___   ___  | |_ ___    _ __ ___  _   _| | ___| |_| |_ ___  | | | | | |\n   \\ \\/  \\/ / _ | |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\  | '__/ _ \\| | | | |/ _ | __| __/ _ \\ | | | | | |\n    \\  /\\  |  __| | (_| (_) | | | | | |  __/ | || (_) | | | | (_) | |_| | |  __| |_| ||  __/ |_| |_| |_|\n     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  |_|  \\___/ \\__,_|_|\\___|\\__|\\__\\___| (_) (_) (_)\n")
#credits
credits = 100
while credits > 0:
    while userCheck == 'n':
        #===============================================================================================================================================================================================
        #initialize
        isOdd = None
        isLow = None
        correct = None
        #===============================================================================================================================================================================================
        #display credits
        print("\033[1;37mYou have",credits,"credits. ")
        #===========================================================================================================================================================================================
        #choice
        while True:
            gameMode = input("Do you want to bet on:\n1: Whether the number is odd or even\n2: What range the number will be in \n3: A specific range of numbers \n4: if the number will be 0 or 00\n5: If the number will be black or red\nInput what gamemode you want to play(1/2/3/4/5): ")
            if gameMode == '':
                clearscr()
                continue
            try:
                gameMode = int(gameMode)
            except (TypeError,ValueError):
                clearscr()
                print("Please input an integer between 1 and 6.")
                continue
            if gameMode not in range(1,6):
                clearscr()
                print("Please input a valid integer. ")
                continue
            break
        while True:
            try:
                gameMode = int(gameMode)
            except (TypeError,ValueError):
                print("Please input '1' or '2'.")
                pass
            break
        #============================================================================================================================================================================================
        #ask bets
        while True:
            bet = input("How many credits do you want to bet? ")
            try:
                bet = int(bet)
            except (TypeError,ValueError):
                print("Please input an integer")
                continue
            break
        #===========================================================================================================================================================================================
        #check if bet is more than current credits and confirm to continue
        if int(bet) > credits:
            print("You bet more credits than you have!")
        elif bet == credits:
            print("You bet the amount of credits you have!")
        elif bet <= 0:
            print("You bet a negative number!")
        else:
            break
        userCheck = input("Are you sure you want to continue? (y/n) ").lower()
    #==============================================================================================================================================================================================
    #generate number
    #number = random.randint(-1,36)
    number = 0
    #==============================================================================================================================================================================================
    #check if guess is correct
    #odd or even
    if gameMode == 1:
        #checkOdd
        while True:
            evenOrOdd = input("Will the number be even or odd? (even/odd) ").lower()
            if evenOrOdd == "odd":
                guess = True
                break
            elif evenOrOdd == "even":
                guess = False
                break
            else:
                print("Please input 'even' or 'odd'")
                continue
        isOdd = checkOdd(number)
        if guess == isOdd:
            correct = True
        elif guess != isOdd:
            correct = False
        else:
            input("FATAL ERROR\nENTER to exit")
            logging.error("checkOdd failed")
        betIncrease = 1
    #low or high
    elif gameMode == 2:
        while True:
            lowOrHigh = input("Will the number be in: \n1: 1-12\n2: 13-24\n3: 25-36\n4: 1-19\n5: 20-36\n")
            if lowOrHigh != '1' and lowOrHigh != '2' and lowOrHigh != '3' and lowOrHigh != '4' and lowOrHigh != '5':
                print(type(lowOrHigh))
                print("Please input an integer from 1 to 5")
            else:
                lowOrHigh = int(lowOrHigh)
                break
        #checkLow
        if lowOrHigh == 4 or lowOrHigh == 5:
            isLow = checkLow(number)
            betIncrease = 2
            if lowOrHigh == isLow:
                correct = True
            elif lowOrHigh != isLow:
                correct = False
            else:
                input("FATAL ERROR\nENTER to exit ")
                logging.error("checkLow failed")
                sys.exit()
        elif lowOrHigh == 1 or lowOrHigh == 2 or lowOrHigh == 3:
            isRange = checkRange3(number)
            betIncrease = 3
            if lowOrHigh == isRange:
                correct = True
            elif lowOrHigh != isRange:
                correct = False
            else:
                #error code 1
                input("FATAL ERROR\nERROR CODE 1\nENTER to exit")
                logging.error("checkRange3 failed")
                sys.exit()
    #what range
    elif gameMode == 3:
        while True:
            global usrRangeStart
            global usrRangeEnd
            input1 = input("Input the start of the range: ")
            try:
                input1 = int(input1)
            except (TypeError,ValueError):
                print("Please input an integer.")
                continue
            break
        while True:
            input2 = input("Input the end of the range: ")
            try:
                input2 = int(input2)
            except (TypeError,ValueError):
                print("Please input an integer.")
                continue
            break
        if (input2 in range(-2,2) and input1 in range(33,37)) or (input1 in range(-2,2) and input2 in range(33,37)):
            clearscr()
            print("Please input a valid range. ")
            continue
        if input1 > input2:
            usrRangeEnd = input1
            usrRangeStart = input2
        else:
            usrRangeEnd = input2
            usrRangeStart = input1
        isInUsrRange = checkUserRange(usrRangeStart,usrRangeEnd,number)
        if isInUsrRange:
            correct = True
        elif not isInUsrRange:
            correct = False
        betIncrease = 3
    #if its zero
    elif gameMode == 4:
        whichZero = ''
        while whichZero != '0' and whichZero != '00':
            whichZero = input("Will the number be 00 or 0: (0/00) ")
            if number == 0 and whichZero == "0":
                correct = True
            elif number == -1 and whichZero == "00":
                correct = True
            else:
                correct = False
        betIncrease = 38
    #red or black
    elif gameMode == 5:
        while redOrBlack != "red" and redOrBlack != "black":
            print("reds: ",reds)
            print("blacks: ",blacks)
            redOrBlack = input("Will the number be a red or a black: (red/black) ").lower()
            correct = checkRed(redOrBlack,number,reds)
    else:
        #shouldn't happen
        print("FATAL ERROR")
        #error code 2
        print("ERROR CODE 2")
        input("ENTER to exit")
        logging.error("should not happen!!!")
        sys.exit()
    if number == -1:
        print("The number is: 00")
    else:
        print("The number is: ",number)
    if correct == True:
        print("You are correct!")
        credits+=int(bet)*betIncrease
    elif correct == False:
        print("You are wrong. :(")
        credits -= int(bet)*betIncrease
    else:
        #error code 3
        print("Unknown Error!!!")
        print("ERROR CODE 3")
        input("Press ENTER to exit")
        sys.exit()
    input("ENTER to continue")
    clearscr()

print("You have",credits,"credits. ")
print("\033[1;31m  _____          __  __ ______    ______      ________ _____  \n / ____|   /\\   |  \\/  |  ____|  / __ \\ \\    / |  ____|  __ \\ \n| |  __   /  \\  | \\  / | |__    | |  | \\ \\  / /| |__  | |__) |\n| | |_ | / /\\ \\ | |\\/| |  __|   | |  | |\\ \\/ / |  __| |  _  / \n| |__| |/ ____ \\| |  | | |____  | |__| | \\  /  | |____| | \\ \\ \n \\_____/_/    \\_|_|  |_|______|  \\____/   \\/   |______|_|  \\_\\")
sys.exit()
print("Error: ExitFailed\nThe code failed to exit. Please redownload the application. If the error continues, please fie an error report and wait for the reply. ")
