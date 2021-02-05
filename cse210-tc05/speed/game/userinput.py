from game import constants
from game.actor import Actor
from game.point import Point

class UserInput(Actor):
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self.inputted_word = []
        self.check_word = ''
        position = Point(1, constants.MAX_Y)

        self.set_position(position)
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")

    def _add_letter(self, letter):
        self.inputted_word.append(letter)
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")
        
    def _clear_letters(self):
        self.inputted_word = []
        self.get_check_word()
        self.set_text(f"Enter word here: {self.check_word}")

    def get_check_word(self):

        self.check_word = ''

        for x in range(len(self.inputted_word)):
            self.check_word = self.check_word + self.inputted_word[x]