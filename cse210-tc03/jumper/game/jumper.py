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
            message = ""# ascii art 
        elif self.fails == 3:
            message = ""# ascii art
        elif self.fails == 2:
            message = ""# ascii art
        elif self.fails == 1:
            message = ""# ascii art
        else: #fails == 0:
            message = ""# put variable here

        return message 

    def updateArray(self, positionsOfCorrect, guess):
        pass