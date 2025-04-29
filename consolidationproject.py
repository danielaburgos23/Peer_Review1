# consolidation project. lock in. let's goooo.

import os
import random

# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["A:1", "2:2", "3:3", "4:4", "5:5", "6:6", "7:7", "8:8", "9:9", "10:10", "J:11", "Q:12"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]

# creating cards here
def create_deck():
    deck = {}
    for value in value:
        for face in face:
            deck.append(value + ' of ' + face)

