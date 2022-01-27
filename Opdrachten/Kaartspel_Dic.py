from random import shuffle,choice

classes = ['harten','klaveren','schoppen','ruiten']
cards = ['aas',2,3,4,5,6,7,8,9,10,'boer','vrouw','heer']

deck,hand = [],[]

for i in range(4):
    if i % 2 == 0:
        deck.append('joker')
    for x in range(13):
        deck.append(f'{classes[i]} {cards[x]}')
deckSize = len(deck)
for y in range(7):
    handPick = choice(deck)
    hand.append(f'kaart {y+1}: {handPick}')
    deck.remove(handPick)
    deckSize -= 1
    shuffle(deck)
print(*hand,sep='\n')
print(f'\ndeck ({len(deck)} kaarten):\n{deck}')