class Display:
    def __init__(self):
        displayText = ''

    def displayMain(self, roster, board):

        self.displayText = ""

        self.displayText = "\n--------------------"
        self.displayText += (f"\nPlayer {roster.player1}: {board._guess1}, {board._hint1}")
        self.displayText += (f"\nPlayer {roster.player2}: {board._guess2}, {board._hint2}")  
        self.displayText += "\n--------------------"

        return self.displayText

    def displayWinner(self, winnerName):

        self.displayText = ""

        self.displayText = "\n" + str(winnerName) + " won!"

        return self.displayText