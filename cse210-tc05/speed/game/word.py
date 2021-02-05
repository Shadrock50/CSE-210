import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """Word is the word that the user must type. The responsibility of Word is to keep track of its appearance
         and position. 

    Stereotype:
        Structurer, Information Holder

    Attributes: 
        _points (integer): The number of points the word is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (something) figure something to put here
        """
        super().__init__() 
        self._points = 0
        self._word = constants.LIBRARY[random.randint(0 , len(constants.LIBRARY))]
        # print(constants.LIBRARY)
        self.set_text(self._word) 
        self.set_velocity(random.randint(constants.MIN_V, constants.MAX_V))
        self.reset()

    def get_points(self):
        return self._points

    def reset(self):
        """changes the position to a random one within the boundaries of the screen and reassigns the points to 
            the length of the word typed.
        
        Args:
            position (integer(s)): the position to change.
            points (integer): The points to add.

        Returns:

        """
        self._points = len(self._word) #does this work for a stretch goal?
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x,y)

        self.set_position(position)