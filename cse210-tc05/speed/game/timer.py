from game.actor import Actor
from game.point import Point
import sys

class Timer(Actor):
    """Time left. The responsibility of Time is to keep track of the time left.

    Stereotype:
        Information Holder

    Attributes: 
        _time_remaining (integer): The time left remaining
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Time): an instance of Time.
        """
        super().__init__()
        self._time_remaining = 1000
        position = Point(1, 1)
        self.set_position(position)
        self.set_text(f"Time Remaining: {self._time_remaining}")
    
    def subtract_time(self):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Time): An instance of Time.
        """
        self._time_remaining = self._time_remaining - 1
        self.set_text(f"Time Remaining: {self._time_remaining}")

    def check_time(self):

        if self._time_remaining == 0:
            sys.exit()