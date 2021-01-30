

class Check:
    def __init__(self):
        self.player1Victory = False
        self.player2Victory = False
        
    
    

    # The result array will init a player1Victory, and a player2Victory, both of which will be false. 
# It will then have three functions: A check to see if anyone won, and will return both variables either way, 
# a display function if no one won, which will display the results without ending the game, and a function to 
# display the winners name and end the game



    def checkVictory(self, board): #add the array to be passed in
        # write stuff here 

        for i in board._code:
            if board.guess1[i] != board._code[i]:
                self.player1Victory = True
            else:
                self.player1Victory = False

        for i in board._code:
            if board.guess2[i] != board._code[i]:
                self.player2Victory = True
            else:
                self.player2Victory = False

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
        pass

    def display(self): 
        pass
