from game.roster import Roster
import random

class Board:
    def __init__(self):
        self._code = []
        self._guess = [-,-,-,-]
        self._hint = [*,*,*,*]
        self._prepare()

    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        board = "\n--------------------"
        for i in roster._players:
            board += (f"\nPlayer {i}: {self._guess}, {self._hint}")
        board += "\n--------------------"
        return board


    def _create_hint(self, guess):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.

    Returns:
        string: A hint in the form [xxxx]
    """ 
        for index, letter in enumerate(guess):
            if code[index] == letter: 
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
    
    def _prepare(self):
        """Sets up the board with 4 random numbers.
        
        Args:
            self (Board): an instance of Board.
        """
        for i in range(4):
            i = random.randint(1, 9)
            self._code.append(i)