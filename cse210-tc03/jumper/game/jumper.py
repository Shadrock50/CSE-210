import random

class Jumper:
    """A game of hangman with a twist. The responsibility of this class is to keep track of the
    users guesses and times failed as they try to guess the word that is ramdomly chosen from
    a large list.

    Stereotype:
        Information Holder

    Attributes:
        answer (list): The users letter guesses
        fails (integer): The number of failed guesses
        displayArray (list): The letters ("_") in the random word not guessed by user.
    """
    
    def __init__(self, correctWord):
        """The class constructor. Declares and initializes instance attributes and keeps
        track of the correctWord.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.answer = [] 
        self.fails = 0
        self.displayArray = []
        i = 0

        while i != len(correctWord):
            self.displayArray.append("_") #inserts an underscore for the length of the correct word
            i = i + 1 #iterates i      

    def picture(self):
        """Gets a message from the jumper.

        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            string: A message from the jumper.
        """
        if self.fails == 4:
            message = "\n   x\n  /|\\\n  / \\\n\n^^^^^^^" # dead 
        elif self.fails == 3:
            message = "\n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^" # -3 health
        elif self.fails == 2:
            message = "\n \\   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^" # -2 health
        elif self.fails == 1:
            message = "\n /___\\\n \\   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^" # -1 health
        else: #fails == 0: player is at full health
            message = "  ___\n /___\\\n \\   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^"

        return message 

    def updateArray(self, positionsOfCorrect, guess):
        """Checks to see if the user entered a valid letter that is found in the word.

        Args:
            self (Jumper): An instance of Jumper.
        """
        if not positionsOfCorrect:
            self.fails = self.fails + 1 #Counts a fail if positions array is empty
        else:
            for element in positionsOfCorrect:
                self.displayArray[element] = guess #if not empty, updates the display array

        return

    def checkVictory(self):
        """Checks to see if the user guessed a correct word yet.

        Args:
            self (Jumper): An instance of Jumper.
        """
        checkVictory = False
        checkSum = 0 #checkSum is returned to zero each time we check.

        for element in self.displayArray: #checkSum only iterates if an underscore is found. 
            if element == "_":
                checkSum = checkSum + 1
        
        if checkSum == 0: #Only if checkSum hasn't changed will the victory be triggered. 
            checkVictory = True

        return checkVictory

    def checkDefeat(self):
        """Checks to see if the user has failed four guess attempts.

        Args:
            self (Jumper): An instance of Jumper.
        """
        checkDefeat = False

        if self.fails == 4: #You lose if there are 4 fails. 
            checkDefeat = True

        return checkDefeat