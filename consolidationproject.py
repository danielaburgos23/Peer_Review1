# consolidation project.
import os
import random
import time
from burn_module import burn_card
import pandas as pd
import seaborn as sns


# defining and giving each aspect of the card a value and a face (AKA diamonds, hearts, etc etc)
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen"]
face = ["Hearts", "Diamonds", "Spades", "Clubs"]
used_cards = []

#static values as variables
minimum_score = 1
starting_hand = 8
redraw_cards = 4
earlymax_score = 9
max_score = 17
total_rounds = 17
shoot_moon = 16

value_dict = {"Ace": 1, "2": 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12}
face_dict = {"Hearts": 1, "Diamonds": 2, "Spades": 3, "Clubs": 4}   

# creates a genuine deck with no repeats
def create_deck():
    """

    Creates and shuffles a deck without the Kings face card.
   
    """
    return[f"{v} of {f}" for v in value for f in face]

#dealer function to simulate real dealer mechanics
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
def valid_cards(player_name, hand, lead_face=None):
    """
    
    Makes sure the player picks a valid card from their hand.
    
    """
    while True:
        card = input(f"{player_name}, pick a card please!")
        if card not in hand:
            print("Invalid choice. Please try again.")
            continue
        card_face = card.split(" of ")[1]
        player_lead = False
        for h in hand:
            suit = h.split(" of ")[1]
            if suit == lead_face:
                player_lead = True
                break
        if player_lead and card_face != lead_face:
            print("You must choose a card with the same suit: {lead_face}. Please Try again!: ")
            continue
        hand.remove(card)
        return card
    


# ~~~~~~~~~~~~~~~~~~~~~~~~~ THIS IS WHERE THE GAME BEGINS ~~~~~~~~~~~~~~~~~~~~~~~~~ #


def main():
    deck = create_deck()
    random.shuffle(deck)

    # list of (future) cards in each player's hand 
    play1_hand = []
    play2_hand = []
    
    # dealer mechanic to deal cards and log used cards to prevent reusing
    dealer(play1_hand, starting_hand, deck, used_cards)
    dealer(play2_hand, starting_hand, deck, used_cards)
    
    # scoreboard
    scorep1 = 0
    scorep2 = 0

    # round log for pd/sns datasets
    round_log = []

    round_leader = random.choice(["Player 1", "Player 2"])
    print(f"The Round Leader is... {round_leader}! Congratulations! The Game Will Now Begin!")

    # beginning of game code for loop
    for round_number in range(1, total_rounds, + 1):

        # presents the round number, player 1, and player 2's hands
        print("Round: ", round_number)
        print("Player 1's Hand: ", play1_hand)
        print("\nPlayer 2's Hand: ", play2_hand)
        
        # Gives players time to read their hands and make a decision/strategize/etc
        time.sleep(2.5)

        if round_leader == "Player 1":
            card1 = valid_cards("Player 1's hand: ", play1_hand)
            card2 = valid_cards("Player 2's hand: ", play2_hand) 
        else:
            card2 = valid_cards("Player 2's hand: ", play2_hand) 
            card1 = valid_cards("Player 1's hand: ", play1_hand)
        
        # compares card to determine the lead face card the other player has to follow
        lead_face = face_dict[card1.split(' of ')[1]] if round_leader == "Player 1" else face_dict[card2.split(' of ')[1]]
        results = card_comparison(card1, card2, lead_face, round_leader)

        # for pandas(pd): logs each round's winner for DataFrame
        round_log.append({"Round": round_number, "Winner": results})

        # adds score to scoreboard after every round
        if results == "Player 1":
            print("Player 1 wins this round!")
            # lets players read the prompts, adds better flow to the game
            time.sleep(1.8)
            scorep1 += 1
            round_leader = "Player 1"
        elif results == "Player 2":
            print("Player 2 wins this round!")
            # lets players read the prompts, adds better flow to the game
            time.sleep(1.8)
            scorep2 += 1
            round_leader = "Player 2"

        # presents score to players after every round
        print(f"Scores:\n Player 1: {scorep1}\n Player 2: {scorep2}")

        # gives players to read scoreboard after every round
        time.sleep(1.8)

        # burn module to burn top card at the end of each round
        burn_card(deck, used_cards)

        # redrawing cards on rounds 5 and 9 (when both players have 4 cards left)
        if round_number in [5, 9]:
            dealer(play1_hand, redraw_cards, deck, used_cards)
            dealer(play2_hand, redraw_cards, deck, used_cards)
            
        # special conditions: early ending mechanic
        elif scorep1 == earlymax_score and scorep1 - scorep2 >= 2:
                print("Early Ending! Player 1 Wins!")
                break

        elif scorep2 == earlymax_score and scorep2 - scorep1 >= 2:
                print("Early Ending! Player 2 Wins!")
                break
       
    

    # special conditions: shoot the moon mech
    if  scorep2 == 0 and scorep1 == shoot_moon:
            print("Player 2 shoots the moon and WINS with 17 points!")
            scorep2 = 17
            
    elif  scorep1 == 0 and scorep2 == shoot_moon:
            print("Player 1 shoots the moon and WINS with 17 points!")
            scorep1 = 17
            
    # final scoreboard/decider
    print(f"Final Scores:\n Player 1: {scorep1}\n Player 2: {scorep2}")
    if scorep1 > scorep2:
        print("Player 1 Wins Tricksy Battle! Congratulations!")
    elif scorep2 > scorep1:
        print("Player 2 Wins Tricksy Battle! Congratulations!")
    else:
        print("It's a tie!")
   
    # pd: convert logs to DataFrame and saves to CSV
    df = pd.DataFrame(round_log)
    df.to_csv("round_log.csv", index=False)
    print("Round-by-round log saved to 'round_log.csv'")

    # sns: create and save a visual chart of each round win(s)
    import matplotlib.pyplot as plt
    sns.countplot(x="Winner", data=df)
    plt.title("Rounds Won per Player")
    plt.xlabel("Player")
    plt.ylabel("Rounds Won")
    plt.savefig("rounds_won_chart.png")
    print("Round win chart saved as 'rounds_won_chart.png'")


if __name__ == "__main__":
    main()
