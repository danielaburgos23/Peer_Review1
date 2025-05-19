# consolidation project.
import os
import random
import time
from burn_module import burn_card

# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]
used_cards = []
# deck = []

#static values as variables
starting_hand = 8
redraw_cards = 4
earlymax_score = 9
max_score = 17 #shoot the moon makes it 17
total_rounds = 16

value_dict = {"Ace": 1, "2": 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12}
face_dict = {"Hearts": 1, "Diamonds": 2, "Spades": 3, "Clubs": 4}   

# creating cards function heree (again)
def create_deck():
    """

    Creates and shuffles a standard deck without the Kings face card.
   
    """
    return[f"{v} of {f}" for v in value for f in face]


#other variation of above^ except 100 steps longer
    # complete_deck = []
    # for value_thing in value:
        # for face_thing in face:
            # card = value_thing + ' of ' + face_thing
            # complete_deck.append(card)
    # random.shuffle(complete_deck)
    # return complete_deck

    
#dealer mechanic, come back later, back working on this mech again (5/17)
def dealer(hand, count, deck, used_cards):
    """
    
    Deals a number of cards to a player's hand, 8 in this case.
    
    """
    for xx in range(count):
        if deck:
            card = deck.pop()
            hand.append(card)
            used_cards.append(card)
            

# card breakdown system so each card is genuine (and not copied by storing in the dictionaries afterward)
def card_breakdown(card):
    """
    
    Splits a card string into its # value and face rank to prevent repeat cards.
    
    """
    val, face = card.split(' of ')
    return value_dict[val], face_dict[face]

# card comparison system/callback to decide winners of each round
def card_comparison(card1, card2, lead_face, starting_player):
    """
    
    Compares the two players' cards and returns the round winner.
    
    """
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

# checks to see if player card chosen is valid
def valid_cards(player_name, hand):
    """
    
    Makes sure the player picks a valid card from their hand.
    
    """
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
def main():
    deck = create_deck()
    random.shuffle(deck)

    play1_hand = []
    play2_hand = []

    dealer(play1_hand, starting_hand, deck, used_cards)
    dealer(play2_hand, starting_hand, deck, used_cards)

    scorep1 = 0
    scorep2 = 0

    round_leader = random.choice(["Player 1", "Player 2"])
    print(f"The Round Leader is... {round_leader}! Congratulations! The Game Will Now Begin!")

# beginning of game code blocks

    for round_number in range(1, total_rounds, + 1):

# beginning of if/else/elif game code blocks
        print("Round: ", round_number)
        print("Player 1's Hand: ", play1_hand)
        print("\nPlayer 2's Hand: ", play2_hand)

        if round_leader == "Player 1":
            card1 = valid_cards("Player 1's hand: ", play1_hand)
            card2 = valid_cards("Player 2's hand: ", play2_hand) 
        else:
            card2 = valid_cards("Player 2's hand: ", play2_hand) 
            card1 = valid_cards("Player 1's hand: ", play1_hand)

        # if round_leader == "Player 1":
            # card1 = input("Player 1, choose your card: ")
            # while card1 not in play1_hand:
                # print("Invalid choice. Try again: ")
                # card1 = input("Player 1, choose your card: ")
                # print("Player 1's Hand: ", play1_hand)
            # play1_hand.remove(card1)
            
            # card2 = input("Player 2, choose your card: ")
            # while card2 not in play2_hand:
                # print("Invalid choice. Try again: ")
                # card2 = input("Player 2, choose your card: ")
                # print("Player 1's Hand: ", play1_hand)
            # play2_hand.remove(card2)
        # else:
            # card2 = input("Player 2, choose your card: ")
            # while card2 not in play2_hand:
                # print("Invalid choice. Try again: ")
                # print("Player 1's Hand: ", play1_hand)
            # play2_hand.remove(card2)

            # card1 = input("Player 1, choose your card: ")
            # while card1 not in play1_hand:
                # print("Invalid choice. Try again: ")
                # card1 = input("Player 1, choose your card: ")
                # print("Player 1's Hand: ", play1_hand)
            # play1_hand.remove(card1)
        
        lead_face = face_dict[card1.split(' of ')[1]] if round_leader == "Player 1" else face_dict[card2.split(' of ')[1]]
        results = card_comparison(card1, card2, lead_face, round_leader)

        if results == "Player 1":
            print("Player 1 wins this round!")
            scorep1 += 1
            round_leader = "Player 1"
        elif results == "Player 2":
            print("Player 2 wins this round!")
            scorep2 += 1
            round_leader = "Player 2"

        print(f"Scores:\n Player 1: {scorep1}\n Player 2: {scorep2}")

        # new via module
        burn_card(deck, used_cards)

        time.sleep(2.0)

# redrawing cards on rounds 5 and 9 (when both players have 4 cards left)
        if round_number in [4, 8]:
            dealer(play1_hand, redraw_cards, deck, used_cards)
            dealer(play2_hand, redraw_cards, deck, used_cards)

if __name__ == "__main__":
    main()