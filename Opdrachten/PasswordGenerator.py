import random
from string import ascii_lowercase,ascii_uppercase
from random import randint, choice, shuffle

def oneAndThree(password):
    for i in range(3):
        password.append(choice(ascii_lowercase))

def randomChars(inList):
    specialChars = ('@','#','$','%','&','_','?')
    for i in range(3):
        inList.append(choice(specialChars))

def highCase(inList):
    for i in range(randint(2,6)):
        inList.append(choice(ascii_uppercase))

def lowerCase(inList):
    for i in range(5):
        inList.append(choice(ascii_lowercase))

def numbers(inList):
    number = [0,1,2,3,4,5,6,7,8,9]
    for i in range(randint(4,7)):
        inList.append(choice(number))

def passwordCheck(password):
    if len(password) < 24:
        password.append(choice(ascii_lowercase))
        passwordCheck(password)
    else:
        
        print("here is your password:")


def passwordMaker():
    #lists that are used
    inList = []
    password = []
    #functions used 
    randomChars(inList)
    highCase(inList)
    lowerCase(inList)
    numbers(inList)
    random.shuffle(inList)
    #makes the first 3 letters of password & extends it to the main
    oneAndThree(password)
    password.extend(inList)
    #makes the password the same as in the assignment
    passwordCheck(password)
    #prints the password without ' or []
    print(*password,sep='')

passwordMaker()   
