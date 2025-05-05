
# burn_module.py

# This module provides a reusable function to burn the top card from a deck for the Tricksy Card Game Project

def burn_card(deck, used_cards):
    if deck:
        burned = deck.pop(0)
        used_cards.append(burned)
        print("Top card burned:", burned)
    else:
        print("Deck is empty. Nothing to burn.")
