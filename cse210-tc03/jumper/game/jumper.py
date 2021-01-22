import random

class Jumper: 
    """  """
    def __init__(self, correctWord):
        self.answer = [] 
        self.fails = 0
        self.displayArray = []
        i = 0

        while i != len(correctWord):
            self.displayArray.append("_") #inserts an underscore for the length of the correct word
            i = i + 1 #iterates i      

    def picture(self):
        if self.fails == 4:
            message = "\n   x\n  /|\\\n  / \\\n\n^^^^^^^" # dead 
        elif self.fails == 3:
            message = "\n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^"# -3 health
        elif self.fails == 2:
            message = "\n \   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^" # -2 health
        elif self.fails == 1:
            message = "\n /___\\\n \   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^" # -1 health
        else: #fails == 0: player is at full health
            message = "  ___\n /___\\\n \   / \n  \\ / \n   0\n  /|\\\n  / \\\n\n^^^^^^^"# put variable here

        return message 

    def updateArray(self, positionsOfCorrect, guess):

        if not positionsOfCorrect:
            self.fails = self.fails + 1 #Counts a fail if positions array is empty
        else:
            for element in positionsOfCorrect:
                self.displayArray[element] = guess #if not empty, updates the display array

        return

    def checkVictory(self):
        checkVictory = False
        checkSum = 0 #checkSum is returned to zero each time we check.

        for element in self.displayArray: #checkSum only iterates if an underscore is found. 
            if element == "_":
                checkSum = checkSum + 1
        
        if checkSum == 0: #Only if checkSum hasn't changed will the victory be triggered. 
            checkVictory = True

        return checkVictory

    def checkDefeat(self):
        checkDefeat = False

        if self.fails == 4: #You lose if there are 4 fails. 
            checkDefeat = True

        return checkDefeat