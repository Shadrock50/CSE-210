""" Player Character module
Contains PlayerCharacter class and associated utilities. Used in
controlling main character in gameplay.
Authors:
  - Shad Christopherson
  - Peter Griffin
"""
import arcade
import constants

class PlayerCharacter(arcade.Sprite):
    """A code template for movement of the character. The responsibility of 
    this class of objects is to determine the movement of the main character. 
    
    Stereotype:
        Controller

    Attributes:
        character_face_direction
        cur_texture
        scale
        points
        idle_texture_pair
        walk_textures
    """
    def __init__(self):
        """The class constructor."""

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = constants.CHARACTER_SCALING

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = "images/animated_characters/femaleAdventurer"

        # Load textures for idle standing
        self.idle_texture_pair = self.load_texture_pair(f"{main_path}_idle.png")

        #initialize texture
        self.texture = self.idle_texture_pair[0]

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = self.load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

    def update_animation(self, delta_time: float = 1/60):
        """ Updates the animation each frame """

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return
        else:# Walking animation
            self.cur_texture += 1
            if self.cur_texture > 7 * constants.UPDATES_PER_FRAME:
                self.cur_texture = 0
            frame = self.cur_texture // constants.UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.walk_textures[frame][direction]


    def load_texture_pair(self, filename):
        """loads texture pair"""

        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True)
        ]