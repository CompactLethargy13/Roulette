from time import sleep
import requests
import os
import urllib.request
def clearscr():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system('cls')
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
                whichPage = input("Choose which page you want to go:\n1: Betting multiplier\n2: How to play\n'q' to quit\nInput here: (1/2) ")
                while whichPage != '1' and whichPage != '2' and whichPage != 'q':
                    os.system('cls')
                    os.system('clear')
                    if whichPage != 'repeat':
                        print("Please input 1 or 2")
                    whichPage = input("Choose which page you want to go:\n1: Betting multiplier\n2: Planned changes\n'q' to quit\nInput here: (1/2) ")
                if whichPage == '1':
                    os.system('cls')
                    os.system('clear')
                    print("Betting on even or odd, or red or black    |   1: 1 return")
                    print("Betting on low or high range               |   1: 2 return")
                    print("Betting on a user-specified range          |   1: 3 return")
                    print("Betting on 0 or 00                         |   1:38 return")
                    whichPage = 'repeat'
                    input("ENTER to exit ")
                elif whichPage == '2':
                    plannedChanges()
                elif whichPage == 'q':
                    input("\033[1;37m  ______ _   _ _______ ______ _____    _              _             _   \n |  ____| \\ | |__   __|  ____|  __ \\  | |            | |           | |  \n | |__  |  \\| |  | |  | |__  | |__) | | |_ ___    ___| |_ __ _ _ __| |_ \n |  __| | . ` |  | |  |  __| |  _  /  | __/ _ \\  / __| __/ _` | '__| __|\n | |____| |\\  |  | |  | |____| | \\ \\  | || (_) | \\__ | || (_| | |  | |_ \n |______|_| \\_|  |_|  |______|_|  \\_\\  \\__\\___/  |___/\\__\\__,_|_|   \\__|")
                    break
                break
