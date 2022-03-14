christmasTickets = []

def askNames():
    a = True
    while a == True:
        names = input('What name would you like to add? (Type "STOP" if you dont want to add more names)\n').lower()
        if names == 'stop':
            a = False
            print(christmasTickets)
        else:
            contains_duplicates = any(christmasTickets.count(element) > 1 for element in christmasTickets)
            if contains_duplicates == True:
                del christmasTickets[-1]
            else:
                christmasTickets.append(names)

askNames()
