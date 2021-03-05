import arcade
import constants
import random

class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.power_ups_list = None
        self.wall_list = None
        self.player_list = None #May need enemy list
        self.enemies_list = None #May want list for each enemy type
        self.background_list = None
        self.flag_list = None
        self.bullet_list = None

        self.player_sprite = None

        self.view_bottom = 0
        self.view_left = 0

        self.score = 0
        self.powerup = 0
        self.level = 1
        self.end_of_map = 0

         # Load sounds
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self, level):
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.power_ups_list = arcade.SpriteList(use_spatial_hash=True)
        self.enemies_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList(use_spatial_hash=True)
        self.flag_list = arcade.SpriteList(use_spatial_hash=True)

        image_source = ":resources:images/enemies/mouse.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "map" + str(self.level) + ".tmx" #this is supposed to use the window.level to call in the map
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        power_ups_layer_name = 'Power-ups'
        enemies_layer_name = 'Enemies'
        flag_layer_name = 'Flag'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        self.end_of_map = my_map.map_size.width * constants.GRID_PIXEL_SIZE


        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        # -- Coins
        self.power_ups_list = arcade.tilemap.process_layer(my_map, power_ups_layer_name, constants.TILE_SCALING)

        # Enemies
        self.enemies_list = arcade.tilemap.process_layer(my_map, enemies_layer_name, constants.TILE_SCALING)
        self.generate_enemies()

        # Flag
        self.flag_list = arcade.tilemap.process_layer(my_map, flag_layer_name, constants.TILE_SCALING)

        # -- Background objects
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", constants.TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
       
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, constants.GRAVITY)


    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:            
            if self.physics_engine.can_jump():
                #self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                self.physics_engine.jump(constants.PLAYER_JUMP_SPEED)
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.F:
            self.generate_bullet(self.powerup)
        

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()

        #bullets
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_wall_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(hit_wall_list) > 0:
                bullet.remove_from_sprite_lists()
            if bullet.left > self.view_left + constants.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

        #move enemies

        self.enemies_list.update()
        self.move_enemies()
                
            # if enemy.Health == 2:
                # enemy.change_x = constants.CRAWLER_SPEED
        


        # # See if we hit any coins
        # coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # # Loop through each coin we hit (if any) and remove it
        # for coin in coin_hit_list:
        #     # Remove the coin
        #     coin.remove_from_sprite_lists()
        #     # Play a sound
        #     arcade.play_sound(self.collect_coin_sound)
        #     self.score += 1

        changed = False

          # Did the player fall off the map or collide with enemy?
        if (self.player_sprite.center_y < -100) or (arcade.check_for_collision_with_list(self.player_sprite, self.enemies_list)):
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed = True
            arcade.play_sound(self.game_over)


          # See if the user got to the flag
        if arcade.check_for_collision_with_list(self.player_sprite, self.flag_list):
            # Advance to the next level
            self.level += 1

            # Load the next level
            self.setup(self.level)

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed = True

        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)
    
    def generate_enemies(self):
        pass
        # for enemy in self.enemies_list:
        #     if enemy.properties['type'] == 'Crawler':
        #         enemy.health = 2
        #     elif enemy.properties['type'] == 'Flier':
        #         enemy.health = 3
        #     elif enemy.properties['type'] == 'Jumper':
        #         enemy.health = 3
    
    def move_enemies(self):
        for enemy in self.enemies_list:
            if enemy.properties['type'] == 'Crawler':
                enemy.change_x = -1
                jumpint = random.randint(0, 10)
                if jumpint == 10:
                    enemy.change_y == 5

    def generate_bullet(self, powerup):
        if powerup == 0:
            bullet = arcade.Sprite(":resources:images/space_shooter/laserblue01.png", constants.SPRITE_SCALING_LASER)
            bullet.change_x = constants.BULLET_SPEED


            bullet.center_y = self.player_sprite.center_y
            bullet.center_x = self.player_sprite.center_x #position of the bullet
            self.bullet_list.append(bullet)


    def on_draw(self):

        arcade.start_render()
        self.wall_list.draw()
        self.background_list.draw()
        self.bullet_list.draw()
        self.enemies_list.draw()
        self.flag_list.draw()
        self.power_ups_list.draw()
        self.player_list.draw()

         # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)
