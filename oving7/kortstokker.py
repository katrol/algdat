from sys import stdin
from itertools import repeat

def merge(decks):
    word = []
    done = False
    while done == False:
        done = True
        smallest = None
        for deck in xrange(len(decks)):
            if (decks[deck] != [] and (smallest == None or decks[deck][0][0] < decks[smallest][0][0])):
                done = False
                smallest = deck
        if done == True:
            break
        word.append(decks[smallest][0][1])
        decks[smallest].pop(0)
    return ''.join(word)
        

   

def main():
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks.append(deck)
    print(merge(decks))

main()
