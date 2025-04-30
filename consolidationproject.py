# consolidation project. lock in. let's goooo.

import os
import random

# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]

value_dict = {"Ace":1, "2":2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12}
face_dict = {"Hearts":1, "Diamonds":2, "Spades":3, "Clubs":4}
test_card = ["Ace", "Hearts"]

# creating cards function heree
def create_deck():
    deck = {}
    for value in value:
        for face in face:
            card = value + ' of ' + face
            deck.append(card)
    
#dealer mechanic, come back later ***********
def dealer(hand, deck):
    for xx in range(8):
        hand.append(deck.pop())

def randomize_card():
    xy = random.choice(value)
    xyz = random.choice(face)
    card = xy + ' of ' + xyz
    return card




# CHECK LIST
# create deck - done 
# define hand deck
# shuffling mechanic
# dealing mech too? - maybe? recheck later
# while if elif else loop for rounds
# actual thing to combine the two defintions (value, face)
### .split using "of" to combine 
# 

