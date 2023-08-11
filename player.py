# author: Dhruv Shukla
# date: May 1, 2023
# file: player.py a Python program that implements a player class for Tic Tac Toe Game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

import random


# Player Class
# Class made for 1v1 amongst two player, 1 v AI and 1 vs Unbeatable AI (MiniMax)
class Player:
    from board import Board
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        return self.sign
        # return an instance sign

    def get_name(self):
        return self.name
        # return an instance name

    def choose(self, board):
        # use the methods board.isempty(cell), and board.set(cell, sign)
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        while True:
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, updates the board
            cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n').upper()
            if cell in valid_choices:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    return
                # if user chooses incorrectly
                # prints a message that the input is wrong and rewrite the prompt
                else:
                    print("You did not choose correctly.\n")
            else:
                print("You did not choose correctly.\n")


# An AI Class that can play with the Player
# The class inherits from Player Class
# The AI chooses its moves at random
class AI(Player):
    from random import choice
    from board import Board
    # initialising values
    def __init__(self, name, sign, board):
        self.name = name
        self.sign = sign
        self.board = board.board
        self.valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    # Returns the sign of AI
    def get_sign(self):
        return self.sign

    # return an the name of the Player
    def get_name(self):
        return self.name

    #randomly chooses a move to be played
    def choose(self, board):
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        while True:
            cell = random.choice(valid_choices)
            print((f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:{cell} \n'))
            if board.isempty(cell):
                board.set(cell, self.sign)
                break
            else:
                continue

# An unbeatable AI Class using a recursive approach
class MiniMax(AI):
    import board  # getting the board from class Board
    def __init__(self, name, sign, board):  # initalising the values
        # inherits initalisation from AI Class
        super().__init__(name, sign, board)
        # decides the sign of the player playing
        if self.sign == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'

    # A function choose to select the move
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    # MiniMax function
    # Calculates every possible move and returns the best move available
    # Unbeatable AI
    def minimax(self, board, self_player, start):
        minscore = float('inf')
        maxscore = float('-inf')
        move = ''
        best_move = None
        available_moves_var = board.availableMoves()
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # self is a looser (opponent is a winner)
            elif board.get_winner() == self.opponent:
                return -1
            # is a tie
            else:
                return 0
        else:
            if self_player:
                # Iterates through every available move and updates best move
                for move in available_moves_var:
                    if board.isempty(move):
                        board.set(move, self.sign)
                        # Recursive call part of the function
                        score = self.minimax(board, False, False)
                        board.set(move, " ")
                        # best move is updated if score is better than previous best move
                        if score > maxscore:
                            maxscore = score
                            best_move = move

            else:
                # Iterates through every available move and updates best move
                for move in available_moves_var:
                    if board.isempty(move):
                        board.set(move, self.opponent)
                        # Recursive call part of the function
                        score = self.minimax(board, True, False)
                        board.set(move, " ")
                        # best move is updated if score is better than previous best move
                        if score < minscore:
                            minscore = score
                            best_move = move

        if start:
            return best_move
        # is a tie
        elif self_player:
            return maxscore
        # self is a looser (opponent is a winner)
        else:
            return minscore


# Smart AI Made using Heuristic Approach
class SmartAI(AI):
    def __init__(self, name, sign, board):  # initalising the values
        super().__init__(name, sign, board)

        # Choose function plays the required move

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n")
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        if self.sign == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'
        # While loop checks for all the different conditions
        while True:

            if self.board[0] == self.board[1] == self.sign and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break

            elif self.board[3] == self.board[4] == self.sign and self.board[5] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[6] == self.board[7] == self.sign and self.board[8] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break

            elif self.board[1] == self.board[2] == self.sign and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[4] == self.board[5] == self.sign and self.board[3] == ' ':
                board.set(valid_choices[3], self.sign)
                print(valid_choices[3])
                return True
                break

            elif self.board[0] == self.board[2] == self.sign and self.board[1] == ' ':
                board.set(valid_choices[1], self.sign)
                print(valid_choices[1])
                return True
                break

            elif self.board[3] == self.board[5] == self.sign and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break

            elif self.board[6] == self.board[8] == self.sign and self.board[7] == ' ':
                board.set(valid_choices[7], self.sign)
                print(valid_choices[7])
                return True
                break
            elif self.board[6] == self.board[0] == self.sign and self.board[3] == ' ':
                board.set(valid_choices[3], self.sign)
                print(valid_choices[3])
                return True
                break

            elif self.board[1] == self.board[7] == self.sign and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break

            elif self.board[2] == self.board[8] == self.sign and self.board[5] == ' ':
                board.set(valid_choices[5], self.sign)
                print(valid_choices[5])
                return True
                break

            elif self.board[4] == self.board[1] == self.sign and self.board[7] == ' ':
                board.set(valid_choices[7], self.sign)
                print(valid_choices[7])
                return True
                break
            elif self.board[2] == self.board[5] == self.sign and self.board[8] == ' ':
                board.set(valid_choices[8], self.sign)
                print(valid_choices[8])
                return True
                break
            elif self.board[3] == self.board[0] == self.sign and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            elif self.board[6] == self.board[3] == self.sign and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[4] == self.board[7] == self.sign and self.board[1] == ' ':
                board.set(valid_choices[1], self.sign)
                print(valid_choices[1])
                return True
                break
            elif self.board[5] == self.board[8] == self.sign and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[0] == self.board[8] == self.sign and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break
            elif self.board[6] == self.board[2] == self.sign and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break
            elif self.board[4] == self.board[0] == self.sign and self.board[8] == ' ':
                board.set(valid_choices[8], self.sign)
                print(valid_choices[8])
                return True
                break
            elif self.board[6] == self.board[4] == self.sign and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[2] == self.board[4] == self.sign and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            elif self.board[8] == self.board[4] == self.sign and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[7] == self.board[8] == self.sign and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            if self.board[0] == self.board[1] == self.opponent and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break

            elif self.board[3] == self.board[4] == self.opponent and self.board[5] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[6] == self.board[7] == self.opponent and self.board[8] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break

            elif self.board[1] == self.board[2] == self.opponent and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[4] == self.board[5] == self.opponent and self.board[3] == ' ':
                board.set(valid_choices[3], self.sign)
                print(valid_choices[3])
                return True
                break

            elif self.board[0] == self.board[2] == self.opponent and self.board[1] == ' ':
                board.set(valid_choices[1], self.sign)
                print(valid_choices[1])
                return True
                break

            elif self.board[3] == self.board[5] == self.opponent and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break

            elif self.board[6] == self.board[8] == self.opponent and self.board[7] == ' ':
                board.set(valid_choices[7], self.sign)
                print(valid_choices[7])
                return True
                break
            elif self.board[6] == self.board[0] == self.opponent and self.board[3] == ' ':
                board.set(valid_choices[3], self.sign)
                print(valid_choices[3])
                return True
                break

            elif self.board[1] == self.board[7] == self.opponent and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break

            elif self.board[2] == self.board[8] == self.opponent and self.board[5] == ' ':
                board.set(valid_choices[5], self.sign)
                print(valid_choices[5])
                return True
                break

            elif self.board[4] == self.board[1] == self.opponent and self.board[7] == ' ':
                board.set(valid_choices[7], self.sign)
                print(valid_choices[7])
                return True
                break
            elif self.board[2] == self.board[5] == self.opponent and self.board[8] == ' ':
                board.set(valid_choices[8], self.sign)
                print(valid_choices[8])
                return True
                break
            elif self.board[3] == self.board[0] == self.opponent and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            elif self.board[6] == self.board[3] == self.opponent and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[4] == self.board[7] == self.opponent and self.board[1] == ' ':
                board.set(valid_choices[1], self.sign)
                print(valid_choices[1])
                return True
                break
            elif self.board[5] == self.board[8] == self.opponent and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[0] == self.board[8] == self.opponent and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break
            elif self.board[6] == self.board[2] == self.opponent and self.board[4] == ' ':
                board.set(valid_choices[4], self.sign)
                print(valid_choices[4])
                return True
                break
            elif self.board[4] == self.board[0] == self.opponent and self.board[8] == ' ':
                board.set(valid_choices[8], self.sign)
                print(valid_choices[8])
                return True
                break
            elif self.board[6] == self.board[4] == self.opponent and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[2] == self.board[4] == self.opponent and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            elif self.board[8] == self.board[4] == self.opponent and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[7] == self.board[8] == self.opponent and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break

            elif self.board[0] == self.board[4] == self.opponent and self.board[8] == ' ':
                board.set(valid_choices[8], self.sign)
                print(valid_choices[8])
                return True
                break
            elif self.board[2] == self.board[4] == self.opponent and self.board[6] == ' ':
                board.set(valid_choices[6], self.sign)
                print(valid_choices[6])
                return True
                break
            elif self.board[6] == self.board[4] == self.opponent and self.board[2] == ' ':
                board.set(valid_choices[2], self.sign)
                print(valid_choices[2])
                return True
                break
            elif self.board[8] == self.board[4] == self.opponent and self.board[0] == ' ':
                board.set(valid_choices[0], self.sign)
                print(valid_choices[0])
                return True
                break
            elif self.board[0] == self.board[2] == self.opponent and self.board[3] == ' ':
                board.set(valid_choices[3], self.sign)
                print(valid_choices[3])
                return True
                break
            # In case above conditions are not met
            # First for Sign == X

            else:
                if self.sign == 'X':
                    if self.board[0] == " ":
                        board.set(valid_choices[0], self.sign)
                        print(valid_choices[0])
                        return True
                        break
                    elif self.board[4] != " ":
                        board.set(valid_choices[3], self.sign)
                        print(valid_choices[3])
                        return True
                        break
                # In case above conditions are not met
                # First for Sign == O
                else:
                    if self.sign == 'O':
                        if self.board[4] == " ":
                            board.set(valid_choices[4], self.sign)
                            print(valid_choices[4])
                            return True
                            break
                        elif self.board[8] == ' ':
                            board.set(valid_choices[8], self.sign)
                            print(valid_choices[8])
                            return True
                            break
