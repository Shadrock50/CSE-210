# copied from rfk
import random
from game import constants
from game.action import Action
from game.point import Point

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
                newDirection = ball.get_velocity().reverse_y()
                ball.set_velocity(newDirection)
                del bricks[iterator] #Still needs to detect whether it hits the side or top/bottom
            iterator += 1           #need to actually delete the brick object, or it'll bounce always

        #Peter do
        #import score
        # walls will need to be another loop for x values on the ceiling and floor

        edgeCheck = ball.get_position().get_x()
        ceilingCheck = ball.get_position().get_y()
        ball.set_text(ceilingCheck)

        if edgeCheck == constants.MAX_X - 1 or edgeCheck == 1:
            newDirection = ball.get_velocity().reverse_x()
            ball.set_velocity(newDirection)

        if ceilingCheck == 1:
            newDirection = ball.get_velocity().reverse_y()
            ball.set_velocity(newDirection)

        if ceilingCheck == constants.MAX_Y - 1:
            pass
            #endgame. I'd do this, but I'm going to bed.

        #christian do
        # put a loop here to check for each instance of paddle

        for i in range(10): #Handles collision with Paddle

            checkPosition = paddle.get_position()
            newPositionToCheck = checkPosition.lengthen_detect(i)

            if ball.get_position().equals(newPositionToCheck):
                # invert the velocity
                newDirection = ball.get_velocity().reverse_y()
                ball.set_velocity(newDirection)

                
                # description = artifact.get_description()
                # marquee.set_text(description) 