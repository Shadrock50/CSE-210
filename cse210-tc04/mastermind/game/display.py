class Display:
    """ Display controls the displaying of the board and winner
    
    Stereotype:
        Converts output to string

    Attributes:
        self(Display): instance of display
        """
    def __init__(self):
        self.displayText = ""

    def displayMain(self, roster, board):
        """Displays the board

    Args:
    self(Display): instance of display
        roster(Roster): instance of roster
        board(Board): instance of board
    """

        self.displayText = ""

        self.displayText = "\n--------------------"
        self.displayText += (f"\nPlayer {roster.player1}: {board._guess1}, {board._hint1}")
        self.displayText += (f"\nPlayer {roster.player2}: {board._guess2}, {board._hint2}")  
        self.displayText += "\n--------------------"

        return self.displayText

    def displayWinner(self, winnerName):
        """Displays the winner

    Args:
        self(Display): instance of display
        winnerName(str): name of the winner
    """

        self.displayText = ""

        self.displayText = "\n" + str(winnerName) + " won!"

        return self.displayText