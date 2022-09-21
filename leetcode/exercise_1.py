#!/usr/bin/env python3

"""
Given an array of characters MxN find the hidden words in the array

The words will be: word = "ABCB", word = "SEE", word = "ABCCED"
The answers will be: False, True, True accordingly
The board will be: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"""


class Board:
    def __init__(self, board):
        self.board = board
        self.x_length = len(self.board[0])
        self.y_length = len(self.board)

    def get_coordinates(self, character):
        """

        Args:
            character: Any letter from a to z

        Returns: All coordinates on which the character appears

        """
        return [(x, y) for y in range(self.y_length)
                for x in range(self.x_length)
                if self.board[y][x] == character]

    def is_character_here(self, character):
        """

        Args:
            character: Any letter

        Returns: True: if the character is in the board
                 False: if the character is not in the board

        """
        for y in range(self.y_length):
            for x in range(self.x_length):
                if self.board[y][x] == character:
                    return True

        return False

    def nuke_coordinate(self, coordinate):
        """

        Args:
            coordinate:

        Returns: boolean True: The coordinate was "nuke"
                         False: The coordinate wasn't "nuke"

        """
        if coordinate[0] < self.x_length and coordinate[1] < self.y_length:
            if self.board[coordinate[1]][coordinate[0]] == '':
                return False
            else:
                self.board[coordinate[1]][coordinate[0]] = ''
                return True
        else:
            return False


def find_word(board, word):
    """

    Args:
        board: A board of MxN cells
        word: Given word to lookout inside the board

    Returns: True: If the word is in the board
             False: If the word is not in the board

    """
    # Confirm if all letters are in the board
    if check_letters_are_available_in_board(board, word):
        for letter in word:
            for y in range(board.y_length):
                for x in range(board.x_length):
                    if board.board[y][x] == letter:
                        # TODO: Finish this functions and test that the code works

    return False


def check_letters_are_available_in_board(board, word):
    for y in range(board.y_length):
        for x in range(board.x_length):
            if not board.is_character_here(board.board[y][x]):
                return False


array_board = Board([["A", "B", "C", "E"],
                     ["S", "F", "C", "S"],
                     ["A", "D", "E", "E"]])

print(array_board.get_coordinates('E'))
find_word(array_board, 'E')
print(array_board.get_coordinates('E'))
## Should be false or word not found
# board_1.is_word_here("ABCB")
## Should be True or word found
# board_1.is_word_here("SEE")
## Should be True or word found
# board_1.is_word_here("ABCCED")
