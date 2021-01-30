import random

class Board:
    """The board manages hints and game-play loop

    Stereotype: 
        Input Management

    Args:
        self(Board): an instance of Board.
    """
    def __init__(self):
        self._code = []
        self._guess1 = ['-','-','-','-']  
        self._guess2 = ['-','-','-','-']  
        self._hint1 = ['*','*','*','*']
        self._hint2 = ['*','*','*','*']
        self._prepare()


    def _create_hint(self, guess, guessCounter):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.
        guess: The players guess being compared
        guessCounter: determines player
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

    def _prepare(self):
        """Sets up the board with 4 random numbers.
        
        Args:
            self (Board): an instance of Board.
        """
        for i in range(4):
            i = random.randint(1, 9)
            self._code.append(i) #Why not just do a random number from 1000 to 9999? Faster than a loop