import random

class Board:
    def __init__(self):
        self._code = []
        self._guess = ['-','-','-','-']  
        self._hint = ['*','*','*','*']
        self._prepare()

    def to_string(self, player):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        board = "\n--------------------"
        for i in player:
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
        #update guess (will need to fix this)
        for i in guess:
            self._guess[i] = i

        for i in guess:
            if self._guess[i] == self._code[i]:
                self._hint[i] = "x"
            elif self._guess[i] in self._code:
                self.hint[i] = "o"
            else:
                self.hint[i] = "*"

        # Lincoln's bit
        # for index, letter in enumerate(guess):
        #     if code[index] == letter: 
        #         hint += "x"
        #     elif letter in code:
        #         hint += "o"
        #     else:
        #         hint += "*"
    
    def _prepare(self):
        """Sets up the board with 4 random numbers.
        
        Args:
            self (Board): an instance of Board.
        """
        for i in range(4):
            i = random.randint(1, 9)
            self._code.append(i)