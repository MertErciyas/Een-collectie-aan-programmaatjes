from sys import stdout
import time,os,sys
from random import randint
from typing import Counter

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")


scoreOneChoice = False
scoreTwoChoice = False
scoreThreeChoice = False
scoreFourChoice = False
scoreFiveChoice = False
scoreSixChoice = False

scoreBoard = {
    'one': 0,
    'two': 0,
    'three': 0,
    'four': 0,
    'four': 0,
    'five': 0,
    'six': 0
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
    loseDice = input("----------------------------------------\ndo you want to remove a dice? (Yes/No)\n----------------------------------------\n").lower()[:1]
    if loseDice == "y":
        removeDice = input("----------------------------------------\nWhich dice would you like to remove?\n----------------------------------------\n")
        try:
            hand.remove(removeDice)
        except ValueError:
            print('Invalid input')
        diceRemover()
    else:
        print("----------------------------------------\nYou decided not to remove a dice. These are your dice:\n----------------------------------------")
        print(hand)
        clearScreen(3)

hand = []

def diceChooser(dices):
    b = input("----------------------------------------\nWhich dice do you choose?\n----------------------------------------\n")
    if b == "":
        print("You chose nothing")
    else:
        z = b.replace(' ','').split(',')
        for x in z:
            if int(x) in diceRoll:
                hand.append(x)
            else:
                print('Please input the numbers that are shown.')
                clearScreen(2)
                workingDice()     

def workingDice():
    if scoreOneChoice == True and scoreTwoChoice == True and scoreThreeChoice == True and scoreFourChoice == True and scoreFiveChoice == True and scoreSixChoice == True:
        print(scoreBoard)
        print("This is your score, you beat the game.")
        exit
    else:
        global hand
        for i in range(3):
            e =  5 - len(hand)
            f = fancyDice(e)
            diceChooser(f) #chooses which dice you want to take
            print(hand)
            diceRemover() #function to remove dice out of your hand
            for x in hand:  
                if not isinstance(x,int):
                    if x.isdigit():
                        d = hand.index(x)
                        hand[d] = int(x)
        print(hand)  
        scoreBoardMaker()

def scoreOneFunction():
    global scoreOneChoice
    scoreOne = input("Would you like to fill the 1's? (y/n)\n").lower()[:1]
    if scoreOne == 'y':
        if scoreOneChoice == False: 
            ones = []
            try:
                for lb in hand:
                    if lb == 1:
                        ones.append(lb)
            except:
                print("Wrong input")
            finally:
                p = sum(ones)
                scoreBoard["one"] = p
                print("",scoreBoard)
                scoreOneChoice = True
                hand.clear()
                workingDice()
        else:
            print("This score is locked!")
            scoreBoardMaker()

def scoreTwoFunction():
        global scoreTwoChoice
        scoreTwo = input("Would you like to fill the 2's? (y/n)\n").lower()[:1]
        if scoreTwo == "y":
            if scoreTwoChoice == False: 
                twos = []
                try:
                    for lb in hand:
                        if lb == 2:
                            twos.append(lb)
                except:
                    print("Wrong input")
                finally:
                    p = sum(twos)
                    scoreBoard["two"] = p
                    print("",scoreBoard)
                    scoreTwoChoice = True
                    hand.clear()
                    workingDice()
            else:
                print("This score is locked!")
                scoreBoardMaker() 

def scoreThreeFunction():
        global scoreThreeChoice
        scoreTwo = input("Would you like to fill the 3's? (y/n)\n").lower()[:1]
        if scoreTwo == "y":
            if scoreThreeChoice == False: 
                threes = []
                try:
                    for lb in hand:
                        if lb == 3:
                            threes.append(lb)
                except:
                    print("Wrong input")
                finally:
                    p = sum(threes)
                    scoreBoard["three"] = p
                    print("",scoreBoard)
                    scoreThreeChoice = True
                    hand.clear()
                    workingDice()
            else:
                print("This score is locked!")
                scoreBoardMaker() 

def scoreFourFunction():
        global scoreFourChoice
        scoreTwo = input("Would you like to fill the 4's? (y/n)\n").lower()[:1]
        if scoreTwo == "y":
            if scoreFourChoice == False: 
                fours = []
                try:
                    for lb in hand:
                        if lb == 4:
                            fours.append(lb)
                except:
                    print("Wrong input")
                finally:
                    p = sum(fours)
                    scoreBoard["four"] = p
                    print("",scoreBoard)
                    scoreFourChoice = True
                    hand.clear()
                    workingDice()
            else:
                print("This score is locked!")
                scoreBoardMaker() 

def scoreFiveFunction():
        global scoreFiveChoice
        scoreTwo = input("Would you like to fill the 5's? (y/n)\n").lower()[:1]
        if scoreTwo == "y":
            if scoreFiveChoice == False: 
                fives = []
                try:
                    for lb in hand:
                        if lb == 5:
                            fives.append(lb)
                except:
                    print("Wrong input")
                finally:
                    p = sum(fives)
                    scoreBoard["five"] = p
                    print("",scoreBoard)
                    scoreFiveChoice = True
                    hand.clear()
                    workingDice()
            else:
                print("This score is locked!")
                scoreBoardMaker() 

def scoreSixFunction():
        global scoreSixChoice
        scoreSix = input("Would you like to fill the 6's? (y/n)\n").lower()[:1]
        if scoreSix == "y":
            if scoreSixChoice == False: 
                sixs = []
                try:
                    for lb in hand:
                        if lb == 6:
                            sixs.append(lb)
                except:
                    print("Wrong input")
                finally:
                    p = sum(sixs)
                    scoreBoard["six"] = p
                    print("",scoreBoard)
                    scoreSixChoice = True
                    hand.clear()
                    workingDice()
            else:
                print("This score is locked!")
                scoreBoardMaker() 


def scoreBoardMaker():
    global scoreBoard
    scoreOneFunction()
    scoreTwoFunction()
    scoreThreeFunction()
    scoreFourFunction()
    scoreFiveFunction()
    scoreSixFunction()


       
def main():
    workingDice()

main()