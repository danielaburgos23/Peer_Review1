# Tricksy Battle Card Game
##### BY: Matt Lahr

This is a Python-based game project for INST126, built to demonstrate understanding of core programming concepts such as functions, conditionals, dictionaries, input validation, random imports, and modularization.

## Objective

Two players go head-to-head in a strategic card game. Each round, both players select a card from their hand to play. The higher card of the **leading suit** wins the round. The game includes bonus rules like card redrawing, burning cards, early win conditions, and the Shoot the Moon mechanic.

## How to Run

1. Clone or download the repo.
2. Open a terminal in the project directory.
3. Run the main script:

## Files Included

- `consolidationproject.py` – game script
- `burn_module.py` – Helper module used to burn the top card of the deck
- `README.txt` – This documentation file

## Key Features

- Modular code structure
- Custom card deck generation
- Burn mechanism after every round
- Card breakdown via value/suit dictionaries
- Randomized starting player via coin flip
- Redraw cards at rounds 5 and 9
- Special End conditions:
  - 9-1 win triggers early victory
  - 16-0 win triggers Shoot the Moon (17-point win)

## Concepts Demonstrated (Pattern Checklist Highlights)

- Function definitions  
- Loops (for, while)  
- Conditionals (if/elif/else)  
- Input validation  
- Dictionaries for lookup  
- Use of lists (deck, hand, used_cards)  
- Modular file (`burn_module`)  
- Use of constants and configuration values  
- Basic randomness (`random.choice`)  
- Game persistence across rounds

## Known Limitations

- Game is strictly two-player and requires exact manual inputs (e.g., "Queen of Hearts")
- No GUI -- it's all terminal-based

## Acknowledgements
- Bug prevents cards from being listed even after reiterations/bug fixes have being made.
- Worked plenty of hours trying to make it work but I couldn't in the end. Very frustrating considering how close I was to making this work but I learned a lot from this project so I am still satisfied with the script I had built. 
