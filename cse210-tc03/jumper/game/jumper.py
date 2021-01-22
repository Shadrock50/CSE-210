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
        pass