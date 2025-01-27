# copied from snake
from game.timer import Timer
from time import sleep
from game import constants, input_service
from game.word import Word
from game.score import Score
from game.userinput import UserInput

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        userinput (UserInput): The users input.
        timer (Timer): The remaining time left.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self.words = []
        for x in range(5): #Generates 5 word actors
            newWord = Word()
            self.words.append(newWord)

        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._userinput = UserInput()
        self._timer = Timer()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means checking the letters the user types.

        Args:
            self (Director): An instance of Director.
        """
        self.input_letter = self._input_service.get_letter()


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking the words for correctness and subtracting
        time.

        Args:
            self (Director): An instance of Director.
        """

        self._move_words()
        self._handle_letter_input()
        self._check_words()
        self._timer.subtract_time()
        self._timer.check_time()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means drawing everything to the screen.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self.words) 
        self._output_service.draw_actor(self._timer)       
        self._output_service.draw_actor(self._userinput)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_words(self): 
        """Handles the checking of words as they are typed.

        Args:
            self (Director): An instance of Director.
        """

        for x in range(5):

            if self._userinput.check_word == self.words[x]._word:
                self._score.add_points(self.words[x]._points)
                self.words[x].reset()
                self._userinput._clear_letters()


    def _move_words(self):
        """Handles moving the words around the screen.

        Args:
            self (Director): An instance of Director.
        """

        for x in range(len(self.words)):   
            self.words[x].move_next()

    def _handle_letter_input(self):
        """Handles adding letters to an array as they are typed.

        Args:
            self (Director): An instance of Director.
        """

        if self.input_letter == "":
            pass
        elif self.input_letter == "*":
            self._userinput._clear_letters()
        else:
            self._userinput._add_letter(self.input_letter)

    
