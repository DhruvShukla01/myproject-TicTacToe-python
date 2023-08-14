# Tic Tac Toe Game with AI

Play the classic Tic Tac Toe game with an exciting twist: challenge yourself against a computer AI with varying difficulty levels!

<img width="262" alt="Screenshot 2023-08-14 at 5 25 27 AM" src="https://github.com/DhruvShukla01/myproject-TicTacToe-python/assets/135282874/871f2140-5309-42ad-b569-2671a01a0266">

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [In-depth File Breakdown](#in-depth-file-breakdown)
- [License](#license)

## Introduction

Tic Tac Toe, also known as Noughts and Crosses, is a timeless strategy game that pits two players against each other. Players take turns marking spaces in a 3x3 grid. The goal? Be the first to get three of your markers in a row, whether it's horizontally, vertically, or diagonally.

In this digital rendition, you can challenge a computer AI that scales in intelligence. From random moves to a heuristic-driven approach, test your mettle against varying levels of difficulty!

## Features
- Interactive command-line interface.
- Two distinct AI difficulty levels:
  - **Basic AI**: Perfect for beginners, makes random moves.
  - **MiniMax**: Uses Recursive Minimax Algorithm to create an unbeatable AI.
  - **Smart AI**: Advanced heuristic analysis ensures a tougher challenge.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository:
   ```bash
   git clone [repo-link]
   ```
2. Navigate to the directory
   ```
   cd [directory-name]
   ```
3. **Running the Game**
   Execute the tictac.py game file:
   ``` bash
   python tictac.py
   ```

## Project File Structure

Below is a brief outline of the project's directory structure and file descriptions:

- **`main.py`**: Controls the overall game progression, from initialization to completion.
  
- **`board.py`**: Defines the `Board` class which manages the tic-tac-toe board's state, ensuring moves are valid, displaying the current board, and checking for game-ending conditions.
  
- **`ai.py`**: Houses the logic for the basic AI opponent, making decisions randomly from available spots.
  
- **`smartai.py`**: Implements the more challenging AI opponent, making decisions based on strategic analysis of the board.
  
- **`README.md`**: A documentation file that provides insights, usage guidelines, and other pertinent information about the game.

## In-depth File Breakdown

Each file in the project has a specific role to ensure smooth gameplay. Below is a breakdown of what each file does:

### `main.py`
This is the heart of our game. Here's what it does:

- **Game Loop**: Controls the main game loop, ensuring that the game progresses in the correct order.
- **User Interaction**: Manages prompts to the user and retrieves user inputs.
- **Game Initialization**: Sets up the game board, determines which player (human or AI) goes first, and initializes the chosen AI difficulty.

### `board.py`
This file manages the core of the Tic Tac Toe game – the board.

- **`Board` Class**: The class that represents the game board.
  - **Display**: Handles the visualization of the board to the console.
  - **Validity**: Checks if a move is valid (i.e., if a chosen cell is unoccupied).
  - **Win/Draw Conditions**: Evaluates the board to check if there's a winner or if the game is a draw.

### `ai.py`
Your computer opponent's brain for the basic difficulty level.

- **Random Move Generation**: When it's the AI's turn, this logic randomly selects an available spot on the board for its move.

### `smartai.py`
This is where the game gets challenging. The advanced AI logic resides here.

- **Heuristic Evaluation**: Uses algorithms to analyze the board and determine the value of each possible move.
  - **Immediate Wins**: If there's a move that leads to an immediate win, the AI takes it.
  - **Blocking Player's Wins**: Identifies potential winning moves for the human player and blocks them.
  - **Strategic Play**: Uses a set of predefined strategies (like center and corner play) to make its move when there are no immediate wins or blocking moves available.

## License

Theis project is licensed under the [BSD 2-Clause License](LICENSE)


