

class Check:
    def __init__(self):
        self.player1VictoryCount = 0
        self.player2VictoryCount = 0
        self._validGuess = False
        
    
    

# The result array will init a player1Victory, and a player2Victory, both of which will be false. 
# It will then have three functions: A check to see if anyone won, and will return both variables either way, 
# a display function if no one won, which will display the results without ending the game, and a function to 
# display the winners name and end the game



    def checkVictory(self, board): #add the array to be passed in
        # write stuff here 

        self.player1VictoryCount = 0
        self.player2VictoryCount = 0
        i = 0
        while i < 4:
            if board._hint1[i] == 'x':
                self.player1VictoryCount = self.player1VictoryCount + 1

            else:
                self.player1Victory = False

            i = i + 1

        i = 0
        while i < 4:
            if board._hint2[i] == 'x':
                self.player2VictoryCount = self.player2VictoryCount + 1

            else:
                self.player2Victory = False

            i = i + 1

        return


        # if self.player1Victory or self.player2Victory:
        #     self.displayWinner()
        # else:
        #     self.display() #array to be passed

    def displayWinner(self, displayWinner):
        # if self.player1Victory:
        #     winner = player1
        # else:
        #     winner = player2
        # return winner

        winnerText = "\n" + str(displayWinner) + " won!"
        return winnerText

    def checkGuess(self, guess):

        self._validGuess = False
        isGuessDigit = True

        iterator = 0
        for i in guess:
            if guess[iterator].isdigit():
                pass
            else:
                isGuessDigit = False

            iterator = iterator + 1

        if len(guess) != 4:
            pass
        elif isGuessDigit == False:
            pass
        else:
            self._validGuess = True
        pass