from game.console import Console
from game.roster import Roster
from game.board import Board
from game.check import Check
from game.display import Display

class Driver:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _console(Console): reads and writes needed data
        _keep_playing(boolean): Determines whether to stay in the game play loop
        _roster(Roster): holds and keeps track of players
        _board(Board): Keeps track of hints and comparison - manages game-play variables
        _check(Check): Validates input and victory
        guessCounter(int): Helps determine the next player
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._display = Display()
        self._keep_playing = True
        self._roster = Roster()
        self._board = Board()
        self._check = Check()
        self.guessCounter = 1
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            if n == 0:
                self._roster.player1 = name
            else:
                self._roster.player2 = name
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        # board = self._board.to_string(self._roster) #passes the players list to to_string
        display = self._display.displayMain(self._roster, self._board)
        self._console.write(display)

        # get next player's move
        player = self._roster.get_current()

        self._console.write(f"\n{player}'s turn:")
        guess = self._console.read("What is your guess? ")

        self._check.checkGuess(guess)

        while self._check._validGuess == False:
            self._console.write("Please only enter 4 numbers!")
            guess = self._console.read("What is your guess? ")
            self._check.checkGuess(guess)

        #insert data validation bit here **guess is a string**

        self.guessCounter = self.guessCounter + 1 #starts at 1 and goes to 2 before passing once. The % 2 of 2 is 0 so it works
        self._board._create_hint(guess, self.guessCounter) # update hint and guess arrays in board
        # player.set_move(move) don't think we need this

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._check.checkVictory(self._board)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """

        if self._check.player1VictoryCount == 4:
            displayWinner = self._roster.player1
        elif self._check.player2VictoryCount == 4:
            displayWinner = self._roster.player2
        else:
            displayWinner = ""

        if displayWinner == "":
            pass
        else:
            displayText = self._display.displayWinner(displayWinner)
            self._console.write(displayText)
            self._keep_playing = False
        self._roster.next_player()