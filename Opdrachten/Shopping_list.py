shoppingList = {}

def shoppingListMake():
    askQuestion = input("What would you like on your shoppinglist? (Type stop to stop)\n")
    if askQuestion == "stop":
        print(shoppingList)
    else:        
        if askQuestion in shoppingList:
            shoppingList[askQuestion] += 1
        else:
            shoppingList[askQuestion] = 1
        shoppingListMake()


print(shoppingListMake())
