from sys import stdout
import time,os,sys
from random import randint

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def scoreBoard():
    scoreBoard = {
        'one: 0',
        'two: 0',
        'three: 0',
        'four: 0',
        'four: 0',
        'five: 0',
        'six: 0'
        } 


def fancyDice(diceNum=5):
    global diceRoll
    diceRoll = []
    for i in range(diceNum):
        diceRoll.append(randint(1,6))
        
    diceDict = {
    1:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '},
    2:{1:'|       |',2:'| o     |',3:'| o     |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    3:{1:'|   o   |',2:'|       |',3:'|   o   |',4:'|       |',5:'|   o   |',6:'| o   o |'},
    4:{1:'|       |',2:'|     o |',3:'|     o |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    5:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '}
    }

    for i in range(5): #5 is for the 5 lines that de dice art requiresx
        for args in diceRoll: #loops through the list entries
            stdout.write(diceDict[i+1][args])
            stdout.write('   ')
        stdout.write('\n')
    return diceRoll

def rollDice(num):
    diceList = []
    for i in range(num):
        diceList.append(randint(1,6))
    return diceList

def diceRemover():
    loseDice = input("do you want to remove a dice? (Yes/No)\n").lower()
    if loseDice == "yes":
        removeDice = input("Which dice would you like to remove?\n")
        try:
            hand.remove(removeDice)
        except ValueError:
            print('Invalid input')
        diceRemover()
    else:
        print("You decided not to remove a dice. These are your dice:")
        print(hand)
        clearScreen(5)

hand = []

def diceChooser(dices):
    b = input("Which dice do you choose?\n")
    z = b.replace(' ','').split(',')
    if int(b) in diceRoll:
        for x in z:
            if int(x) in diceRoll:
                hand.append(x)  
    else:
        print('Please input the numbers that are shown.')     

def workingDice():
    global hand
    for i in range(3):
        e =  5 - len(hand)
        f = fancyDice(e)
        print(f)
        diceChooser(f) #chooses which dice you want to take
        print(hand)
        diceRemover() #function to remove dice out of your hand
        for x in hand:  
            if not isinstance(x,int):
                if x.isdigit():
                    d = hand.index(x)
                    hand[d] = int(x)
    print(hand)  



def main():
    workingDice()


main()

