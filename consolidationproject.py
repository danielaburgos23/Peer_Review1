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

# card breakdown system so each card is genuine (and not copied by storing in the dictionaries afterward)
def card_breakdown(card):
    val, face = card.join(' of ')
    return value_dict[val], face_dict[face]

# card comparison system/callback to decide winners of each round
def card_comparison(card1, card2, lead_face, starting_player):
    val1, face1 = card_breakdown(card1)
    val2, face2 = card_breakdown(card2)

# UNFINISHED *****
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

# beginning of game code blocks

for round_number in range(1, 17):

# special conditions: shoot the moon mechanic
    if scorep1 == 16 and scorep2 == 0:
        print("Player 2 shoots the moon and WINS with 17 points!")
    elif scorep2 == 16 and scorep1 == 0:
        print("Player 1 shoots the moon and WINS with 17 points!")
    else:
        print("Final Scores:\n Player 1: {scorep1}\n Player 2: {scorep2}")
    
# special conditions: early ending mechanic
    if scorep1 >= 9 and scorep2 == 1:
        print("Early Ending! Player 1 Wins!")
        break
    elif scorep2 >= 9 and scorep1 == 1:
        print("Early Ending! Player 2 Wins!")
        break

# redrawing cards on rounds 5 and 9 (when both players have 4 cards left)
    if round_number in [5, 9]:
        dealer(play1_hand, 4)
        dealer(play2_hand, 4)

# beginning of if/else/elif game code blocks
    print(f"Round: {round_number}\nPlayer 1's Hand: {play1_hand}\nPlayer 2's Hand: {play2_hand}")

    if round_leader == "Player 1":
        card1 = input("Player 1, choose your card: ")
        while card1 not in play1_hand:
            print("Invalid Choice. Try again: ")
            card1 = input("Player 1, choose your card: ")
        play1_hand.remove(card1)
        

# burn card from deck @ end of each round (remember to put this at the very end of blocks)
    if deck:
        burned = deck.pop(0)
        used_cards = deck.append(burned)
        print(f"Top card burned: {burned}")

     

    








        
    
    
        






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

