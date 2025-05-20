# Tricksy Battle Card Game
##### BY: Matt Lahr

This is a Python-based game project for INST126, built to demonstrate understanding of core programming concepts such as functions, conditionals, dictionaries, input validation, random imports, and modularization.

## Objective

Two players go head-to-head in a strategic card game called 'Tricksy Battle'. Each round, both players select a card from their hand to play. The higher card of the **leading suit** wins the round. The game includes bonus rules like card redrawing, burning cards, early win conditions, and the Shoot the Moon mechanic.

## How to Run

1. Clone or download the repo.
2. Open a terminal in the project directory.
3. Run the main script:

## Files Included

- `consolidationproject.py` – game script
- `burn_module.py` – Helper module used to burn the top card of the deck
- `README.txt` – This documentation file
- `LICENSE` - MIT License for Ethics and Policy
- `round_log.csv` - Example round dataset results
- `rounds_won_chart` - Example round chart results

## Key Features

- Modular code structure
- Custom card deck generation
- Burn *imported module* to burn top card(s)
- Card breakdown via value/suit dictionaries
- Randomized starting player via coin flip
- Redraw cards at rounds 5 and 9
- Special End conditions:
  - 9-1 win triggers early victory
  - 16-0 win triggers Shoot the Moon (17-point win)

## Advanced Features

- Pandas (pd) dataset & import
- Seaborn (sns) chart & import
- Random import
- MIT License
- Time import

## Known Limitations

- Game is strictly two-player and requires exact manual inputs (e.g., "Queen of Hearts")
- No GUI -- it's all terminal-based
  
