from game import constants
from game.actor import Actor
from game.point import Point

class UserInput(Actor):
    """User input. The responsibility of UserInput is to keep track of what the user types.

    Stereotype:
        Information Holder

    Attributes: 
        inputted_word (array): The characters the user types in an array
        check_word (str): The characters the user types in a string
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes inputted_word, and check_word.
        Sets the position and updates the text.
        
        Args:
            self (UserInput): an instance of UserInput.
        """
        super().__init__()
        self.inputted_word = []
        self.check_word = ''

        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")

    def _add_letter(self, letter):
        """Adds the inputted characters to the array then string and updates the text.
        
        Args:
            self (UserInput): An instance of UserInput.
        """
        self.inputted_word.append(letter)
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")
        
    def _clear_letters(self):
        """Clears the inputted_word, check_word and updates the text.
        
        Args:
            self (UserInput): An instance of UserInput.
        """
        self.inputted_word = []
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")

    def get_check_word(self):
        """Converts the inputted word array into a string.
        
        Args:
            self (UserInput): An instance of UserInput.
        """

        self.check_word = ''

        for x in range(len(self.inputted_word)):
            self.check_word = self.check_word + self.inputted_word[x]