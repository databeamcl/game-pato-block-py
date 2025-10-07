# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PatoBlock Game is a block-stacking arcade game developed in Python using Pygame. The game features a Tetris-like mechanic where players must align falling blocks with existing blocks to continue playing.

## Development Commands

### Running the Game
```bash
python main.py
```

### Installing Dependencies
```bash
pip install -r requirements.txt
```

### Creating Executable
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## Architecture Overview

### Core Game Structure
- **main.py**: Single-file game containing all game logic, organized into three main scenes (menu=0, game=1, game_over=2)
- **GameState class**: Centralized state management (main.py:37-70) that coexists with global variables for backward compatibility
- **Scene-based architecture**: Game flow managed through menu variable (0=main menu, 1=playing, 2=game over)

### Key Components

#### State Management (main.py:37-89)
- `GameState` class centralizes game variables
- Global variables maintained for compatibility
- State synchronization between class and globals

#### Game Mechanics
- **Block Matrix System**: 18x19 grid for game area
  - `block_matrix_main`: Background decoration blocks
  - `block_matrix_game`: Active game blocks
- **Block Alignment Logic** (main.py:242-278): Checks if placed blocks align with previous row
- **Dynamic Difficulty**: Velocity increases with level progression

#### Utility Classes
- **Position class** (util/position.py): Converts matrix coordinates to screen pixels
  - `cal_pos_x(x)`: Matrix X to screen X
  - `cal_pos_y(y)`: Matrix Y to screen Y  
  - Constants: BLOCK_SIZE=32, BASE_X=320, BASE_Y=600
- **Sound class** (util/sound.py): Manages music for different game states
  - Scene-specific music: main menu, gameplay, game over
  - Volume control and mute functionality

### Game Flow Logic

#### Scene Management
- **scene_main()**: Main menu with credit system
- **scene_game()**: Active gameplay with timer and block mechanics
- **scene_game_over()**: End screen

#### Controls
- Main Menu: 1=play, 2=exit, i=insert coin
- Game: Enter=place block, Esc=return to menu
- Game Over: Esc=return to menu

### Resource Structure
- **resources/**: Contains all game assets
  - Images: background, blocks (red/blue/yellow), icons
  - Audio: MIDI files for different game states
  - Block colors array for visual variety

## Development Notes

### Code Style
- Comprehensive docstrings on all major functions
- Spanish language used in comments and documentation
- Exception handling in main game loop
- FPS display for debugging (main.py:456-459)

### Performance Considerations
- 60 FPS target with pygame clock
- Matrix bounds checking to prevent index errors
- Efficient rendering with scene-specific drawing

### Testing
- No formal test framework
- Manual testing through gameplay
- Debug information displayed on screen (FPS, level, blocks remaining)

## Common Patterns

When modifying game logic:
1. Update both GameState class and global variables for compatibility
2. Add bounds checking for matrix operations
3. Use Position class methods for coordinate conversion
4. Handle pygame events in scene-specific keyboard functions
5. Update CHANGELOG.md with version information following existing format

The codebase uses a transitional architecture where GameState coexists with global variables, allowing gradual modernization while maintaining functionality.