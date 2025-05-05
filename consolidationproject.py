# consolidation project. lock in. let's goooo.

import os
import random

# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]
used_cards = []
deck = []

#static values as variables
starting_hand = 8
redraw_cards = 4
earlymax_score = 9
max_score = 17 #shoot the moon makes it 17
total_rounds = 16

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
    val, face = card.split(' of ')
    return value_dict[val], face_dict[face]

# card comparison system/callback to decide winners of each round
def card_comparison(card1, card2, lead_face, starting_player):
    val1, face1 = card_breakdown(card1)
    val2, face2 = card_breakdown(card2)

# burn card function
def burn_card():
    if deck:
        burned = deck.pop(0)
        used_cards.append(burned)
        print("Top card burned: ", burned)

# function to potentially help bug fix
def valid_cards(player_name, hand):
    while True:
        card = input(f"{player_name}, pick a card please!")
        if card in hand:
            hand.remove(card)
            return card
        print("Invalid choice. Please try again.")
        


# UNFINISHED *****
    # if face1 == face2:
        # if val1 > val2:
            # return "Player 1"
        # elif val2 > val1:
            # return "Player 2"
        # else:
            # return starting_player
    # elif face1 == lead_face and face2 != lead_face:
        # return "Player 1"
    # elif face2 == lead_face and face1 != lead_face:
        # return "Player 2"

# ~~~~~~~~~~~~~~~~~~~~~~~~~ THIS IS WHERE THE GAME BEGINS ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

play1_hand = []
play2_hand = []

dealer(play1_hand, starting_hand)
dealer(play2_hand, starting_hand)
scorep1 = 0
scorep2 = 0
round_leader = random.choice(["Player 1", "Player 2"])
print(f"The Round Leader is... {round_leader}! Congratulations! The Game Will Now Begin!")

# beginning of game code blocks

for round_number in range(1, total_rounds, + 1):

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
        dealer(play1_hand, starting_hand)
        dealer(play2_hand, starting_hand)

# beginning of if/else/elif game code blocks
    print(f"Round: {round_number}\nPlayer 1's Hand: {play1_hand}\nPlayer 2's Hand: {play2_hand}")

    if round_leader == "Player 1":
        card1 = input("Player 1, choose your card: ")
        while card1 not in play1_hand:
            print("Invalid choice. Try again: ")
            card1 = input("Player 1, choose your card: ")
            print("Player 1's Hand: ", play1_hand)
        play1_hand.remove(card1)
        
        card2 = input("Player 2, choose your card: ")
        while card2 not in play2_hand:
            print("Invalid choice. Try again: ")
            card2 = input("Player 2, choose your card: ")
            print("Player 1's Hand: ", play1_hand)
        play2_hand.remove(card2)
    else:
        card2 = input("Player 2, choose your card: ")
        while card2 not in play2_hand:
            print("Invalid choice. Try again: ")
            card2 = input("Player 2, choose your card: ")
            print("Player 1's Hand: ", play1_hand)
        play2_hand.remove(card2)

        card1 = input("Player 1, choose your card: ")
        while card1 not in play1_hand:
            print("Invalid choice. Try again: ")
            card1 = input("Player 1, choose your card: ")
            print("Player 1's Hand: ", play1_hand)
        play1_hand.remove(card1)
        
    lead_face = face_dict[card1.split(' of ')[1]] if round_leader == "Player 1" else face_dict[card2.split(' of ')[1]]
    results = card_comparison(card1, card2, lead_face, round_leader)

    if results == "Player 1":
        print("Player 1 wins this round!")
        scorep1 += 1
        round_leader = "Player 1"
    elif results == "Player 2":
        print("Player 1 wins this round!")
        scorep1 += 1
        round_leader = "Player 2"

    print(f"Scores:\n Player 1: {scorep1}\n Player 2: {scorep2})


# burn card from deck @ end of each round (remember to put this at the very end of blocks)