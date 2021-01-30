
class Roster:
    """A collection of players. The responsibility of Roster is to keep track of the players.
    
    Stereotype: 
        Information Holder

    Attributes:
        self(Roster): an instance of Roster.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.current = 2
        self.player1 = ""
        self.player2 = ""
        

    def get_current(self):
        """Gets the current player object.
        
        Args:
            self (Roster): An instance of Roster.
        
        Returns:
            Player: The current player.
        """
        playerName = ""

        if self.current % 2 == 0:
            playerName = self.player1
        else:
            playerName = self.player2



        return playerName
    
    def next_player(self):
        """Advances the turn to the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """        
        self.current = self.current + 1


