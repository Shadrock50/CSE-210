

class Check:
    """Validates a victory and input

    Stereotype: 
        Information Validator

    Args:
        self(Check): an instance of Check.

    """
    def __init__(self):
        self.player1VictoryCount = 0
        self.player2VictoryCount = 0
        


    def checkVictory(self, board): #add the array to be passed in
        """Validates a victory 

    Args:
        self(Check): an instance of Check.
        board(Board): an instance of Board.

    """

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


    def displayWinner(self, displayWinner):
        """Validates a input

    Args:
        self(Check): an instance of Check.
        displayWinner(str): winning players name.

    """

        winnerText = "\n" + str(displayWinner) + " won!"
        return winnerText

    def display(self): 
        pass
