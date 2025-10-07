# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PatoBlock is a block-stacking arcade game built with Python and Pygame. The game follows a classic arcade cabinet style with coin insertion mechanics, where players stack blocks horizontally trying to align them with the previous row. Misaligned blocks reduce the available block size until game over.

## Running the Game

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the game:**
```bash
python main.py
```

**Build executable (optional):**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## Architecture

### Core Game Structure

The game uses a state machine architecture with three main screens (menus):
- Menu 0: Main menu (coin insertion, play/exit options)
- Menu 1: Active gameplay
- Menu 2: Game over screen

### Main Components

**main.py** (468 lines)
- Entry point and main game loop (lines 468-476)
- GameState class centralizes all game state (lines 37-68)
- Three scene handlers: `scene_main()`, `scene_game()`, `scene_game_over()`
- Block matrix system: 18x19 grid for game area
- `render()` function (lines 433-465) manages the rendering pipeline and runs at 60 FPS

**util/position.py**
- Position class handles coordinate transformations
- Converts between matrix indices (0-18 rows, 0-18 columns) and screen pixels
- Block size: 32x32 pixels
- Base coordinates: (320, 600)

**util/sound.py**
- Sound class manages background music for different game states
- Three music tracks: main menu, gameplay, game over
- Includes volume control and mute functionality

### Game Mechanics

**Block Matrix System:**
- `block_matrix_main`: Displayed in main menu (random pattern)
- `block_matrix_game`: Active gameplay grid (18 rows x 19 columns)
- Blocks move horizontally across rows; player presses Enter to place them

**Block Placement Logic:**
- Initial block size: 5 units
- When blocks are misaligned with the row below, `blocks_size_init` decreases (check_blocks() in main.py:242-278)
- Game ends when `blocks_size_init` reaches 0

**Time Management:**
- Each game session has 51 seconds (set in main.py:363)
- Time countdown shown during gameplay with color warnings
- Game ends when time runs out or blocks run out

**Coin System:**
- Players must insert coins (press 'i') to play
- One coin consumed per game session
- Coins tracked in GameState.coins

### Key Functions

**Movement and Collision:**
- `move_blocks_matrix()` (main.py:180-232): Handles block movement and velocity
- `check_blocks()` (main.py:242-278): Validates block alignment and updates block count
- Velocity increases with floor level: `velocity = 100 - (floor * 6)`

**State Management:**
- `reset_game()` (main.py:140-153): Resets all game variables
- Global variables synchronized with GameState instance for backward compatibility

## Resources

All assets located in `resources/`:
- **Images:** icon.png, fondoarcade.png, back.png, block_red.png, block_blue.png, block_yellow.png
- **Audio:** musica.mid (main menu), dk-island-swing.mid (gameplay), playing.mid (game over)

## Development Notes

- The codebase uses both global variables and a GameState class during transition to better state management
- Matrix indexing: Rows are Y-axis (0-17), columns are X-axis (0-18)
- Screen resolution: 1261x663 pixels
- FPS debugging info displayed in top-left corner
