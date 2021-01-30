import random

class Board:
    def __init__(self):
        self._code = []
        self._guess1 = ['-','-','-','-']  
        self._guess2 = ['-','-','-','-']  
        self._hint1 = ['*','*','*','*']
        self._hint2 = ['*','*','*','*']
        self._prepare()

    def to_string(self, roster):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        board = "\n--------------------"
        board += (f"\nPlayer {roster.player1}: {self._guess1}, {self._hint1}")
        board += (f"\nPlayer {roster.player2}: {self._guess2}, {self._hint2}")  
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

        if guessCounter % 2 == 0:
            iterator = 0
            for i in guess:
                self._guess1[iterator] = guess[iterator]
                iterator = iterator + 1

            iterator = 0
            for i in guess:
                if int(self._guess1[iterator]) == int(self._code[iterator]):
                    self._hint1[iterator] = "x"

                else: 
                    checkIterator = 0
                    located = False
                    for i in self._code:
                        if int(self._guess1[iterator]) == int(self._code[checkIterator]):
                            located = True
                        else:
                            pass

                        checkIterator = checkIterator + 1

                    if located == True:
                        self._hint1[iterator] = 'o'
                    else:
                        self._hint1[iterator] = '*'
                iterator = iterator + 1

        else:
            iterator = 0
            for i in guess:
                self._guess2[iterator] = guess[iterator]
                iterator = iterator + 1

            iterator = 0
            for i in guess:
                if int(self._guess2[iterator]) == int(self._code[iterator]):
                    self._hint2[iterator] = "x"

                else: 
                    checkIterator = 0
                    located = False
                    for i in self._code:
                        if int(self._guess2[iterator]) == int(self._code[checkIterator]):
                            located = True
                        else:
                            pass

                        checkIterator = checkIterator + 1

                    if located == True:
                        self._hint2[iterator] = 'o'
                    else:
                        self._hint2[iterator] = '*'
                iterator = iterator + 1

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
            self._code.append(i) #Why not just do a random number from 1000 to 9999? Faster than a loop