import random

class Board:
    def __init__(self):
        self._code = []
        self._guess1 = ['-','-','-','-']  
        self._guess2 = ['-','-','-','-']  
        self._hint1 = ['*','*','*','*']
        self._hint2 = ['*','*','*','*']
        self._prepare()

    def to_string(self, players):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        board = "\n--------------------"
        board += (f"\nPlayer {players[0]}: {self._guess1}, {self._hint1}")
        board += (f"\nPlayer {players[1]}: {self._guess2}, {self._hint2}")  
        board += "\n--------------------"
        return board


    def _create_hint(self, guess, guessCounter):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.

    Returns:
        string: A hint in the form [xxxx]
    """ 
        #update guess (will need to fix this)

        if guessCounter % 2 == 1:
            for i in guess:
                self._guess1[i] = i

            for i in guess:
                if self._guess1[i] == self._code[i]:
                    self._hint1[i] = "x"
                elif self._guess1[i] in self._code:
                    self._hint1[i] = "o"
                else:
                    self._hint1[i] = "*"
        else:
            for i in guess:
                self._guess2[i] = i

            for i in guess:
                if self._guess2[i] == self._code[i]:
                    self._hint2[i] = "x"
                elif self._guess2[i] in self._code:
                    self._hint2[i] = "o"
                else:
                    self._hint2[i] = "*"

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