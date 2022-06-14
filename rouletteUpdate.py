__version__ = "0.7"
#====================================================================================================================================================================================================
#how to use ansi codes:
#print("\033[1;{ANSI_CODE} texts texts")
#include choice of:
#high or low (done)
#odd or even (done)
#or range of number
#====================================================================================================================================================================================================
#import
import random
import sys
import requests
import urllib.request
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#function
def checkOdd(num):
    if (num%2) == 0:
        return False
    else:
        return True
def checkLow(num):
    if num in range(0,19):
        return True
    elif num in range(19,37):
        return False
def userCheck(yesNo):
    global usrCheck
    if yesNo == "y":
        usrCheck = True
    else:
        usrCheck = False
def checkUserRange(start,end,num):
    if num in range(start,end):
        return True
    else:
        return False
#self update
response = requests.get('https://raw.githubusercontent.com/CompactLethargy13/Roulette/main/version.txt')
data = response.text
def check_updates():
    try:
        response = requests.get('https://raw.githubusercontent.com/CompactLethargy13/Roulette/main/version.txt')
        data = response.text
        if float(data) > float(__version__):
            print('Software Update Available!')
            print('Update!{__version__} needs to update to version {data}')
            while True:
                toUpdate = input("Do you want to update now? If no, this will be updated next time.(y/n):").lower()
                if toUpdate == "y" or toUpdate == "n":
                    break
                else:
                    continue
            if toUpdate == "y":
                fileCurrent = open(str(__file__), "r+")
                currentPath = __file__
                url = "https://raw.githubusercontent.com/CompactLethargy13/Roulette/main/rouletteUpdate.py"
                newfilepath, headers = urllib.request.urlretrieve(url, filename = currentPath)
                newFile = open(str(os.getcwd()),"r+")
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
            else:
                pass
    except Exception as e:
        print('Software Update, Unable to Check for Update, Error:' + str(e))

#===================================================================================================================================================================================================
#game starts
print("\033[1;31m __          __  _                            _                          _      _   _         _   _   _  \n \\ \\        / / | |                          | |                        |\
 |    | | | |       | | | | | |\n  \\ \\  /\\  / ___| | ___ ___  _ __ ___   ___  | |_ ___    _ __ ___  _   _| | ___| |_| |_ ___  | | | | | |\n   \\ \\/  \\/ / _ | |/ __/ _ \\| '_ ` _ \\ / _ \\ | __\
/ _ \\  | '__/ _ \\| | | | |/ _ | __| __/ _ \\ | | | | | |\n    \\  /\\  |  __| | (_| (_) | | | | | |  __/ | || (_) | | | | (_) | |_| | |  __| |_| ||  __/ |_| |_| |_|\n     \\/  \\/ \\___|_|\\___\\\
___/|_| |_| |_|\\___|  \\__\\___/  |_|  \\___/ \\__,_|_|\\___|\\__|\\__\\___| (_) (_) (_)\n")
#credits
credits = 100
while credits > 0:
    #===============================================================================================================================================================================================
    #initialize
    isOdd = None
    isLow = None
    correct = None
    #===============================================================================================================================================================================================
    #display credits
    print("\033[1;37mYou have",credits,"credits. ")
    #===============================================================================================================================================================================================
    #ask for input
    usrCheck = False
    while usrCheck == False:
        #===========================================================================================================================================================================================
        #choice
        while True:
            gameMode = input("Do you want to bet on:\n1: Whether the number is odd or even\n2: What range the number will be in \n3: A specific range of numbers \nInput what gamemode you want to \
play(1/2/3): ")
            while True:
                try:
                    gameMode = int(gameMode)
                except (TypeError,ValueError):
                    print("Please input '1' or '2'.")
                    pass
                break
            if gameMode == 2:
        #============================================================================================================================================================================================
                while True:
                    lowOrHigh = input("Will the number be in the low range(1-19) or in the high range(19-36)?\nInput 1 for low range and 2 for high range: ")
                    if lowOrHigh == "1":
                        lowOrHigh = True
                    elif lowOrHigh == "2":
                        lowOrHigh = False
                    else:
                        print("Please input '1' or '2'")
                        continue
                    break
                break
        #odd or even
            elif gameMode == 1:
                while True:
                    evenOrOdd = input("Will the number be even or odd?(even/odd) ").lower()
                    if evenOrOdd == "odd":
                        guess = True
                    elif evenOrOdd == "even":
                        guess = False
                    else:
                        print("Please input 'even' or 'odd'")
                        continue
                    break
                break
            elif gameMode == 3:
                while True:
                    while True:
                        global usrRangeStart
                        global usrRangeEnd
                        usrRangeStart = input("Input the start of the range: ")
                        try:
                            usrRangeStart = int(usrRangeStart)
                        except (TypeError,ValueError):
                            print("Please input an integer.")
                            continue
                        break
                    while True:
                        usrRangeEnd = input("Input the end of the range: ")
                        try:
                            usrRangeEnd = int(usrRangeEnd)
                        except (TypeError,ValueError):
                            print("Please input an integer.")
                            continue
                        break 
                    if usrRangeStart in range(0,2) and usrRangeEnd in range(35,37):
                        print("This range is invalid. Please input a valid range")
                        continue
                    break
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
            userCheck(input("Are you sure you want to continue? (y/n) ").lower())
        elif bet == credits:
            print("You bet the amount of credits you have!")
            userCheck(input("Are you sure you want to continue? (y/n) ").lower())
        elif bet <= 0:
            print("You bet a negative number!")
            userCheck(input("Are you sure you want to continue? (y/n) ").lower())
        else:
            usrCheck = True
    #==============================================================================================================================================================================================
    #generate number
    number = random.randint(0,36)
    #==============================================================================================================================================================================================
    #check if guess is correct
    #odd or even
    if gameMode == 1:
        #checkOdd
        isOdd = checkOdd(number)
        if guess == isOdd:
            correct = True
        else:
            correct = False
    #low or high
    elif gameMode == 2:
        #checkLow
        isLow = checkLow(number)
        if lowOrHigh == isLow:
            correct = True
        elif lowOrHigh != isLow:
            correct = False
    #what range
    elif gameMode == 3:
        isInUsrRange = checkUserRange(usrRangeStart,usrRangeEnd,number)
        if isInUsrRange:
            correct = True
        elif not isInUsrRange:
            correct = False
    else:
        #shouldn't happen
        print("FATAL ERROR")
        sys.exit()
    print("The number is: ",number)
    if correct == True:
        print("You are correct!")
        credits+=int(bet)
    elif correct == False:
        print("You are wrong. :(")
        credits -= int(bet)
    else:
        print("Unknown Error!!!")
        print("Press ENTER to exit")
        input()
        sys.exit()

print("You have",credits,"credits. ")
print("\033[1;31m  _____          __  __ ______    ______      ________ _____  \n / ____|   /\\   |  \\/  |  ____|  / __ \\ \\    / |  ____|  __ \\ \n| |  __   /  \\  | \\  / | |__    | |  | \\ \
\\  / /| |__  | |__) |\n| | |_ | / /\\ \\ | |\\/| |  __|   | |  | |\\ \\/ / |  __| |  _  / \n| |__| |/ ____ \\| |  | | |____  | |__| | \\  /  | |____| | \\ \\ \n \\_____/_/    \\_|_|  |_|______|\
  \\____/   \\/   |______|_|  \\_\\")
