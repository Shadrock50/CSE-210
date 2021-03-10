import arcade
import constants

class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = 'right'

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = constants.CHARACTER_SCALING

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = ":resources:images/enemies/mouse.png"

        # Load textures for idle standing
        self.idle_texture_pair = self.load_texture_pair(f"{main_path}_idle.png")

        # # Load textures for walking
        # self.walk_textures = []
        # for i in range(8):
        #     texture = self.load_texture_pair(f"{main_path}_walk{i}.png")
        #     self.walk_textures.append(texture)

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == 'right':
            self.character_face_direction = 'left'
        elif self.change_x > 0 and self.character_face_direction == 'left':
            self.character_face_direction = 'right'

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]

    def load_texture_pair(self, filename):

        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True)
        ]