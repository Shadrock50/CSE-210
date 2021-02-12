# copied from rfk
import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # ball 
        paddle = cast["paddle"][0] # paddle
        bricks = cast["brick"] # brick
        # marquee.set_text("")
        iterator = 0
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks[iterator].set_text("")
            iterator += 1
                
                # destroy brick object here
                # bounce the ball here (reverses y for top to bottom of brick, x direction for sides)
        # walls will need to be another loop for x values on the ceiling and floor

        # put a loop here to check for each instance of paddle
        if ball.get_position().equals(paddle.get_position()):
            # invert the velocity
            newPosition = ball.reverse_y
            ball.set_velocity(newPosition)

                
                # description = artifact.get_description()
                # marquee.set_text(description) 