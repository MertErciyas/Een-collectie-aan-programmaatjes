import random

kerstLootjesCheck = []

def lootjesMaker():
    b = True
    while b == True:
        names = input("What names would you like to add? (Type STOP if you would like to stop)\n").lower()
        if names == 'stop':
            if len(kerstLootjesCheck) >= 2:
                if len(kerstLootjesCheck) % 2 == 0:
                    b = False
                    print(f"These are the names right now:\n{kerstLootjesCheck}\n----------------------------------") # everything thats in the list  
                    kerstLootjeAfmaker()
        else:
            if names not in kerstLootjesCheck:
                kerstLootjesCheck.append(names)
                lootjesMaker()
            else:
                print(end='')

n = 2

def kerstLootjeAfmaker():
    random.shuffle(kerstLootjesCheck)
    final = [kerstLootjesCheck[i * n:(i + 1) * n] for i in range((len(kerstLootjesCheck) + n - 1) // n )] 
    print(*final,sep=", ") # shuffled list print
    exit()


lootjesMaker()