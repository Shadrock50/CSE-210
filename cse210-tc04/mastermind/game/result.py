# The result array will init a player1Victory, and a player2Victory, both of which will be false. 
# It will then have three functions: A check to see if anyone won, and will return both variables either way, 
# a display function if no one won, which will display the results without ending the game, and a function to 
# display the winners name and end the game

class Result:
    def __init__(self):
        self.player1Victory = False
        self.player2Victory = False

    def checkVictory(self): #add the array to be passed in
        # write stuff here 

        if player1Victory or player2:
            self.displayWinner()
        else:
            self.display() #array to be passed

    def displayWinner(self):
        if player1Victory:
            winner = player1
        else:
            winner = player2
        return winner

    def display(self): #