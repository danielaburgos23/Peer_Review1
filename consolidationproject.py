# consolidation project. lock in. let's goooo.

import os
import random

# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]
used_cards = []
deck = []
value_dict = {"Ace":1, "2":2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12}
face_dict = {"Hearts":1, "Diamonds":2, "Spades":3, "Clubs":4}
test_card = ["Ace", "Hearts"]

# creating cards function heree (again)
def create_deck():
    complete_deck = []
    for value_thing in value:
        for face_thing in face:
            card = value_thing + ' of ' + face_thing
            complete_deck.append(card)
        random.shuffle(complete_deck)
        return complete_deck
            
    
#dealer mechanic, come back later, UPDATE cannot make it static to 8, considering the rules of the game give 4 fresh cards every 4 rounds
def dealer(hand, count):
    for xx in range(count):
        if deck:
            card = deck.pop()
            used_cards.append(card)
            hand.append(deck.pop())

def card_breakdown(card):
    val, face = card.join(' of ')
    return value_dict[val], face_dict[face]

def card_comparison(card1, card2, lead_face):
    val1, face1 = card_breakdown(card1)
    val2, face2 = card_breakdown(card2)

    if face1 == face2:
        if val1 > val2:
            return "Player 1"
        elif val2 > val1:
            return "Player 2"
        else:
            return starting_player
    elif face1 == lead_face and face2 != lead_face:
        return "Player 1"
    elif face2 == lead_face and face1 != lead_face:
        return "Player 2"

# ~~~~~~~~~~~~~~~~~~~~~~~~~ THIS IS WHERE THE GAME BEGINS ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

play1_hand = []
play2_hand = []

dealer(play1_hand, 8)
dealer(play2_hand, 8)
scorep1 = 0
scorep2 = 0
round_leader = random.choice(["Player 1", "Player 2"])
print(f"The Round Leader is... {round_leader}! Congratulations! The Game Will Now Begin!")





        
    
    
        






# save for later maybe 
# def randomize_card():
    # while True:
        # xy = random.choice(value)
        # xyz = random.choice(face)
        # card = xy + ' of ' + xyz
        # if card not in used_cards:
            # used_cards.append(card)
            # return card




# CHECK LIST
# coin flip mechanic for who goes first
# dealing mech too? - DONE
# while if elif else loop for rounds - next 

