from sys import stdout
from random import randint

def fancyDice(diceNum=5):
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

    for i in range(5): #5 is for the 5 lines that de dice art requires
        for args in diceRoll: #loops through the list entries
            stdout.write(diceDict[i+1][args])
            stdout.write('   ')
        stdout.write('\n')
 
def scoreBoard():
    scoreBoard = {'one: 0','two: 0','three: 0','four: 0','four: 0','five: 0','six: 0'}

fancyDice()