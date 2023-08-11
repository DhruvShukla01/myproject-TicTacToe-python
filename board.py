# author: Dhruv Shukla
# date: May 1, 2023
# file: board.py a Python program that implements a Board class for Tic Tac Toe Game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ''

    def get_size(self):
        return self.size
        # optional, return the board size (an instance size)

    def get_winner(self):
        return self.winner
        # return the winner's sign O or X (an instance winner)

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        index = valid_choices.index(cell)
        self.board[index] = sign

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        valid_choices_copy = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        i = valid_choices_copy.index(cell)
        # check if the cell is empty or not
        if self.board[i] != ' ':
            return False
        return True

    def availableMoves(self):
        # returns a list of moves available on the board (used for AI classes)
        available_moves_var = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        return available_moves_var

    # Function checks all the terminating conditions for the game
    def isdone(self):
        done = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        if self.board[0] == self.board[3] == self.board[6] != ' ':  # column 1 condition
            done = True
            self.winner = self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] != ' ':  # column 2 condition
            done = True
            self.winner = self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != ' ':  # column 3 condition
            done = True
            self.winner = self.board[2]
        elif self.board[0] == self.board[1] == self.board[2] != ' ':  # row 1 condition
            done = True
            self.winner = self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] != ' ':  # row 2 condition
            done = True
            self.winner = self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] != ' ':  # row 3 condition
            done = True
            self.winner = self.board[6]
        elif self.board[0] == self.board[4] == self.board[8] != ' ':  # diagonal condition 1
            done = True
            self.winner = self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != ' ':  # diagonal condition 2
            done = True
            self.winner = self.board[2]
        # Tie Condition
        else:
            if ' ' in self.board:
                done = False
            else:
                done = True
                self.winner = ' '
        # depending on conditions assign the instance var winner to O or X
        return done

    def show(self):
        # draws the Tic Tac Toe Board
        print('\n   A   B   C  ')
        print(' +---+---+---+')
        print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
        print(' +---+---+---+')
        print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
        print(' +---+---+---+')
        print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
        print(' +---+---+---+')
