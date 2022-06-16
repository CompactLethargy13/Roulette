from time import sleep
import requests
import os
import urllib.request
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
