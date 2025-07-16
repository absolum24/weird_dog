# Dog Game

A simple pygame-based game where you control a dog using WASD keys and special actions.

## Features

- Smooth dog movement using WASD
- Dog faces left/right as you move
- Eat mode (E): dog eats for 4 seconds or until interrupted
- Sit mode (R): dog sits until another key is pressed
- Random mode (F): dog moves randomly until another key is pressed
- Christmas mode (C): toggles Christmas dog skin
- Sign mode (P): dog holds a sign until another key is pressed
- Multiple dog images and animations
- 60 FPS gameplay
- Clean, well-commented code

## Installation

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place the following images in the same folder as the code:
   - `dog.png` (default dog)
   - `dog_eats.png` (dog eating)
   - `dog_sit.png` (dog sitting)
   - `dog_christmas.png` (Christmas dog)
   - `dog_sign.png` (dog with sign)

## How to Play

1. Run the game:
   ```
   python main.py
   ```
   
   Or for backward compatibility:
   ```
   python game.py
   ```

2. Use the following controls:

### Movement
- **W**: Move up
- **A**: Move left (dog faces left)
- **S**: Move down
- **D**: Move right (dog faces right)

### Special Actions
- **E**: Eat mode (dog eats for 4 seconds or until another key is pressed)
- **R**: Sit mode (dog sits until another key is pressed)
- **F**: Random mode (dog moves randomly until another key is pressed)
- **C**: Toggle Christmas mode (dog uses Christmas skin until C is pressed again)
- **P**: Sign mode (dog holds a sign until another key is pressed)
- **ESC**: Quit the game
- **X Button**: Close the window

### Priority of Modes
- **Sit** and **Eat** take priority over all other modes.
- **Sign** and **Christmas** modes are mutually exclusive and only show if not eating or sitting.
- Movement, eating, sitting, random, Christmas, and sign modes can be interrupted by pressing any other action key as described above.

## Game Features

- Window size: 800x600 pixels
- Dog size: 25% of original image size (scaled down)
- Movement speed: 5 pixels per frame
- Frame rate: 60 FPS

## Project Structure

The game has been refactored into multiple files for better organization:

- `main.py` - Main game entry point
- `config.py` - Game configuration and constants
- `player.py` - Player class with movement and drawing logic
- `game_state.py` - Game state management and window handling
- `game.py` - Legacy file for backward compatibility 