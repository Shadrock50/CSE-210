import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """Food is a nutritious substance that snakes like. The responsibility of Food is to keep track of its appearance
         and position. Food can move around randomly if asked to do so.

    Stereotype:
        Structurer, Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (something) figure something to put here
        """
        super().__init__() 
        self._points = 0
        self._word = constants.LIBRARY[random.randint(0 , len(constants.LIBRARY))]
        self.set_text(self._word) 
        self.set_velocity(constants.MIN_V, constants.MAX_V)
        self.reset()

    def get_points(self):
        return self._points

    def reset(self):
        """changes the position to a random one within the boundaries of the screen and reassigns the points to a random
             number between 1 and 5.
        
        Args:
            position (integer(s)): the position to change.
            points (integer): The points to add.
        """
        self._points = len(self._word) #does this work for a stretch goal?
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x,y)

        self.set_position(position)