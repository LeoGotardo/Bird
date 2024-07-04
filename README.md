# Bird Game

A Python implementation of a Flappy Bird-like game using the Pygame library.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project is a simple clone of the popular Flappy Bird game, developed in Python using the Pygame library. The objective of the game is to navigate the bird through obstacles (pipes) without colliding.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bird-game.git
    cd bird-game
    ```

2. Install the required dependencies:
    ```sh
    pip install pygame
    ```

3. Place the required game assets (images) in a `frames` directory within the project directory. The required assets are:
    - `bird_down.png`
    - `bird_mid.png`
    - `bird_up.png`
    - `background.png`
    - `floor.png`
    - `pipe_top.png`
    - `pipe_bottom.png`
    - `game_over.png`
    - `start.png`

## Usage

Run the game using the following command:
```sh
python bird.py
```

### Controls
- `SPACE`: Start the game / Flap the bird's wings.
- `ESC`: Quit the game.
- `R`: Restart the game after a game over.

## Features

- Flappy Bird-like gameplay
- Score tracking
- Game over and restart functionality
- Animated bird
- Scrolling background and ground

## Dependencies

- Python 3.x
- Pygame

## Configuration

The game configuration includes global variables set within the `Game` class:
- `scroll_speed`: The speed at which the background and obstacles scroll (default: 1).
- `score`: The player's current score (initially 0).
- `win_height`: The height of the game window (default: 720).
- `win_width`: The width of the game window (default: 551).
- `bird_start_position`: The initial position of the bird (default: (100, 250)).

## Documentation

### Classes

- `Game`: Initializes the game, handles the main menu, game loop, and quit functionality.
- `Ground`: Represents the scrolling ground sprite.
- `Bird`: Represents the player's bird character.
- `Pipe`: Represents the top and bottom pipe obstacles.

### Methods

- `Game.__init__()`: Initializes the game, loads images, and sets up the window.
- `Game.quit_game()`: Handles quitting the game.
- `Game.initialize()`: Starts the game loop.
- `Game.menu()`: Displays the main menu.
- `Ground.__init__(x, y, image)`: Initializes a ground segment.
- `Ground.update()`: Updates the ground position.
- `Bird.__init__(image)`: Initializes the bird.
- `Bird.update(user_input)`: Updates the bird's position and handles user input.
- `Pipe.__init__(x, y, image, pipe_type)`: Initializes a pipe.
- `Pipe.update()`: Updates the pipe position and checks for scoring.

## Examples

After cloning the repository and installing dependencies, you can run the game and start playing. Press `SPACE` to make the bird flap and avoid pipes. If the bird hits a pipe or the ground, the game will display a "Game Over" screen. Press `R` to restart.

## Troubleshooting

If you encounter issues with the game, ensure the following:
- Pygame is correctly installed.
- All required image assets are in the `frames` directory.
- You are running the game in a compatible Python environment.

## Contributors

- [Your Name](https://github.com/yourusername)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
