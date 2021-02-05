from game.actor import Actor
from game.point import Point
import sys

class Timer(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._time_remaining = 1000
        position = Point(1, 1)
        self.set_position(position)
        self.set_text(f"Time Remaining: {self._time_remaining}")
    
    def subtract_time(self):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._time_remaining = self._time_remaining - 1
        self.set_text(f"Time Remaining: {self._time_remaining}")

    def check_time(self):

        if self._time_remaining == 0:
            sys.exit()