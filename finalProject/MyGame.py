from arcade.sprite import Sprite
from PlayerCharacter import PlayerCharacter
import arcade
from arcade.sprite_list import check_for_collision
import constants
import time
import random

class MyGame(arcade.View):
    def __init__(self):

        super().__init__()

        self.window.set_mouse_visible(False)
        self.power_ups_list = None
        self.backgrounds_list = None
        self.wall_list = None
        self.player_list = None #May need enemy list
        self.enemies_list = None #May want list for each enemy type
        self.background_list = None
        self.flag_list = None
        self.bullet_list = None
        self.enemy_collisions_list = None
        self.enemy_bullet_list = None

        self.player_sprite = None

        self.view_bottom = 0
        self.view_left = 0

        self.score = 0
        self.powerup = 0
        self.level = 1
        self.end_of_map = 0
        self.powerupTimer = 0
        self.lives = 3
        self.bullet_count = 0
        self.bullet_iterator = 0
        self.i = 0

         # Load sounds
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self, level, lives, score):
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.level = level
        self.lives = lives

        # Keep track of the score
        self.score = score

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.power_ups_list = arcade.SpriteList(use_spatial_hash=True)
        self.enemies_list = arcade.SpriteList()
        self.backgrounds_list = arcade.SpriteList(use_spatial_hash=True)
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList(use_spatial_hash=True)
        self.flag_list = arcade.SpriteList(use_spatial_hash=True)
        self.enemy_collisions_list = arcade.SpriteList(use_spatial_hash=True)

        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 192
        self.player_list.append(self.player_sprite)

        if self.level > 10:
            color = (100, 0, 0)
            arcade.set_background_color(color)

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "map" + str(15) + ".tmx" #use self.level to return the game to normal
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
        self.enemy_collisions_list = arcade.tilemap.process_layer(my_map, "Enemy Collisions", constants.TILE_SCALING)
        self.generate_enemies()

        # Flag
        self.flag_list = arcade.tilemap.process_layer(my_map, flag_layer_name, constants.TILE_SCALING)

        # -- Background objects
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", constants.TILE_SCALING)
        self.backgrounds_list = arcade.tilemap.process_layer(my_map, "Backgrounds", constants.TILE_SCALING)

        # --- Other stuff
        # # Set the background color
        # if my_map.background_color:
        #     arcade.set_background_color(my_map.background_color)
       
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, constants.GRAVITY)


    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:            
            if self.physics_engine.can_jump():
                #self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                self.physics_engine.jump(constants.PLAYER_JUMP_SPEED)
                arcade.play_sound(self.jump_sound)
            self.player_facing = 'up'
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
            self.player_facing = 'down'
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.generate_bullet()
        

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
            self.player_facing = 'right'
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
            self.player_facing = 'right'
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()
        self.player_sprite.update_animation()

        #bullets
        self.bullet_list.update()
        self.enemy_bullet_list.update()
        for bullet in self.bullet_list:
            hit_wall_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(hit_wall_list) > 0:
                bullet.remove_from_sprite_lists()
            if bullet.left > self.view_left + constants.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

            hit_enemy_list = arcade.check_for_collision_with_list(bullet, self.enemies_list)
            if len(hit_enemy_list) > 0:
                bullet.remove_from_sprite_lists()
            for enemy in hit_enemy_list:
                enemy.health = enemy.health - 1
                if enemy.health == 0:
                    enemy.remove_from_sprite_lists()
                    if enemy.properties['type'] == "Crawler":
                        self.score += 100
                    elif enemy.properties['type'] == "Jumper":
                        self.score += 200
                    elif enemy.properties['type'] == "Flier":
                        self.score += 400
                    elif enemy.properties['type'] == "Boss":
                        time.sleep(2)
                        game_view = GameWinView()
                        game_view.setup(self.score, self.player_sprite)
                        self.window.show_view(game_view)

        for bullet in self.enemy_bullet_list:
            hit_wall_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(hit_wall_list) > 0:
                bullet.remove_from_sprite_lists()
            if bullet.left > self.view_left + constants.SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

            if arcade.check_for_collision_with_list(bullet, self.player_list):
                bullet.remove_from_sprite_lists()

                if self.powerup != 3:
                    arcade.play_sound(self.game_over)
                    self.lives = self.lives - 1
                    self.bullet_count = 0
                    self.checkGameOver()
                    time.sleep(1)
                    self.setup(self.level, self.lives, self.score)
                    self.powerup = 0

        #move enemies

        self.enemies_list.update()
        self.updatePowerup()
        self.move_enemies()
        self.shootMultipleBullets()
                

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

        #removes enemies if they fall
        for enemy in self.enemies_list:
            if (enemy.center_y < - 100):
                enemy.remove_from_sprite_lists

          # Did the player fall off the map or collide with enemy?
        if (self.player_sprite.center_y < -100): 
                arcade.play_sound(self.game_over)
                self.lives = self.lives - 1
                self.checkGameOver()
                self.bullet_count = 0
                time.sleep(1)
                self.setup(self.level, self.lives, self.score)
                self.powerup = 0

        
        
        elif arcade.check_for_collision_with_list(self.player_sprite, self.enemies_list):
            # self.player_sprite.center_x = constants.PLAYER_START_X
            # self.player_sprite.center_y = constants.PLAYER_START_Y

            # Set the camera to the start
            # self.view_left = 0
            # self.view_bottom = 0
            # self.powerup = 0
            # changed = True
            if self.powerup != 3:
                arcade.play_sound(self.game_over)
                self.lives = self.lives - 1
                self.bullet_count = 0
                self.checkGameOver()
                time.sleep(1)
                self.setup(self.level, self.lives, self.score)
                self.powerup = 0


          # See if the user got to the flag
        if arcade.check_for_collision_with_list(self.player_sprite, self.flag_list):
            # Advance to the next level
            self.level += 1

            # Load the next level
            
            game_view = LevelView()
            game_view.setup(self.level, self.lives, self.score, self.player_sprite)
            self.window.show_view(game_view)
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
        for enemy in self.enemies_list:
            enemy.hasJumped = False
            enemy.isInAir = False
            enemy.isPhasing = False
            if enemy.properties['type'] == 'Crawler':
                direction = random.randint(0,1)
                if direction == 0:
                    enemy.change_x = constants.CRAWLER_SPEED
                else: 
                    enemy.change_x = -constants.CRAWLER_SPEED
                enemy.health = 3

            elif enemy.properties['type'] == 'Jumper':
                enemy.health = 5

            elif enemy.properties['type'] == 'Flier':
                enemy.health = 2

            elif enemy.properties['type'] == 'Boss':
                enemy.health = 250

    def move_enemies(self):
        for enemy in self.enemies_list:
            if not enemy.properties['type'] == "Flier":
                enemy.change_y += -constants.GRAVITY + .5
            if arcade.check_for_collision_with_list(enemy, self.wall_list):
                enemy.change_y = 0
                #Enemies can get stuck in the ground. This moves them up until they are free. 
                enemy.center_y = enemy.center_y + 1
                enemy.isInAir = False
                
        
        for enemy in self.enemies_list:
            distanceLeft = enemy.left - self.player_sprite.right
            distanceRight = self.player_sprite.left - enemy.right

            if distanceLeft > constants.SCREEN_WIDTH * .9 or distanceRight > constants.SCREEN_WIDTH *.9:
                enemy.change_x = 0
                enemy.change_y = 0

            else:

                if enemy.properties['type'] == 'Crawler':
                    if enemy.change_x == 0:
                        direction = random.randint(0,1)
                        if direction == 0:
                            enemy.change_x = constants.CRAWLER_SPEED
                        else: 
                            enemy.change_x = -constants.CRAWLER_SPEED
                    if arcade.check_for_collision_with_list(enemy, self.enemy_collisions_list):
                        enemy.change_x = enemy.change_x * -1

                if enemy.properties['type'] == 'Boss':
                    generateEnemy = random.randint(0, 150)
                    if generateEnemy == 5:
                        enemyType = random.randint(0,2)
                       
                        if enemyType == 0: 
                            print("Crawler Generated")
                            newEnemy = arcade.Sprite("images/enemies/wormGreen.png", constants.CHARACTER_SCALING)
                            newEnemy.properties['type'] = 'Crawler'
                            newEnemy.center_x = enemy.left
                            newEnemy.center_y = enemy.top
                            newEnemy.change_x = -5
                            newEnemy.change_y = 25

                            self.enemies_list.append(newEnemy)
                            self.generate_enemies()

                        elif enemyType == 1: 
                            print("Jumper Generated")
                            newEnemy = arcade.Sprite("images/enemies/frog.png", constants.CHARACTER_SCALING)
                            newEnemy.properties['type'] = 'Jumper'
                            newEnemy.center_x = enemy.left
                            newEnemy.center_y = enemy.top
                            newEnemy.change_x = -5
                            newEnemy.change_y = 25

                            self.enemies_list.append(newEnemy)
                            self.generate_enemies()

                        elif enemyType == 2: 
                            print("Flier Generated")
                            newEnemy = arcade.Sprite("images/enemies/bee.png", constants.CHARACTER_SCALING)
                            newEnemy.properties['type'] = 'Flier'
                            newEnemy.center_x = enemy.left
                            newEnemy.center_y = enemy.top
                            newEnemy.change_x = -5

                            self.enemies_list.append(newEnemy)
                            self.generate_enemies()

                elif enemy.properties['type'] == 'Flier':

                    distanceUp = enemy.bottom - self.player_sprite.top

                    if arcade.check_for_collision_with_list(enemy, self.wall_list):
                        enemy.change_x = enemy.change_x * -.5
                    #This is a gross nested if statement. But I can't get it to work when combining. 
                    if distanceLeft > -450 and distanceLeft < 450:
                        if distanceUp <= 200 and distanceUp >= -200:
                            if self.player_sprite.right < enemy.left:
                                if enemy.change_x != -constants.FLIER_SPEED:
                                    enemy.change_x = enemy.change_x - .4
                            else: 
                                if enemy.change_x != constants.FLIER_SPEED:
                                    enemy.change_x = enemy.change_x + .4

                            if self.player_sprite.top < enemy.bottom:
                                if enemy.change_y != -constants.FLIER_SPEED / 2:
                                    enemy.change_y = enemy.change_y - .4
                            else:
                                if enemy.change_y != constants.FLIER_SPEED / 2:
                                    enemy.change_y = enemy.change_y + .4
                    else:
                        if enemy.change_x != 0:
                            enemy.change_x = 0
                            enemy.change_y = 0
           

                elif enemy.properties['type'] == 'Jumper':


                    randNum = random.randint(0 , 100)
                    willShoot = random.randint(0,150)
                    if willShoot == 5:
                        enemy_y = enemy._get_center_y()
                        
                        if self.player_sprite.right < enemy.left:
                            bullet = arcade.Sprite("images/animated_characters/frogbullet.png", constants.SPRITE_SCALING_LASER)
                            bullet.angle = 180
                            bullet.center_y = enemy_y
                            bullet.center_x = enemy.left
                            bullet.change_x = -constants.BULLET_SPEED * .7
                            self.enemy_bullet_list.append(bullet)
                        else:
                            bullet = arcade.Sprite("images/animated_characters/frogbullet.png", constants.SPRITE_SCALING_LASER)
                            bullet.angle = 0
                            bullet.center_y = enemy_y
                            bullet.center_x = enemy.right
                            bullet.change_x = constants.BULLET_SPEED * .7
                            self.enemy_bullet_list.append(bullet)

                    if randNum == 5 and enemy.change_y == 0:

                        jumpDirection = random.randint(0,1)
                        if jumpDirection == 1:

                            enemy.change_y = constants.ENEMY_JUMP_SPEED
                            enemy.change_x = constants.JUMPER_SPEED
                            enemy.hasJumped = True
                            enemy.isInAir = True
                        else:
                            enemy.change_y = constants.ENEMY_JUMP_SPEED
                            enemy.change_x = -constants.JUMPER_SPEED
                            enemy.hasJumped = True
                            enemy.isInAir = True
                    
                    if enemy.change_y == 0 and enemy.isInAir == False:
                        enemy.change_x = 0
                        enemy.hasJumped = False

                    
    def shootEnemyBullet(self, enemy):
        if self.player_sprite.right < enemy.left:
            bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
            rotation = 180
            bullet.center_y = enemy.center_y
            bullet.angle = rotation
            bullet.change_x = -constants.BULLET_SPEED
            self.enemy_bullet_list.append(bullet)
        else:
            bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
            rotation = 0
            bullet.center_y = enemy.center_y
            bullet.angle = rotation
            bullet.change_x = constants.BULLET_SPEED
            self.enemy_bullet_list.append(bullet)


    def generate_bullet(self):

        if self.powerup == 0 or self.powerup == 3:
            bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
            rotation = 180
            self.getBulletPositionAndDirection(bullet, rotation)
            self.bullet_list.append(bullet)

        elif self.powerup == 1:
            bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
            bullet2 = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
            bullet3 = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)

            bullet2.change_y = constants.BULLET_SPEED / 3
            bullet3.change_y = -constants.BULLET_SPEED / 3
            bullet2.angle = 18.43
            bullet3.angle = -18.43

            rotation_1 = 180
            rotation_2 = 153.43
            rotation_3 = -153.43

            self.getBulletPositionAndDirection(bullet, rotation_1)
            self.getBulletPositionAndDirection(bullet2, rotation_2)
            self.getBulletPositionAndDirection(bullet3, rotation_3)

            self.bullet_list.append(bullet)
            self.bullet_list.append(bullet2)
            self.bullet_list.append(bullet3)

        elif self.powerup == 2:
            self.bullet_count += 3
            self.bullet_iterator = 0


    def updatePowerup(self):
        for powerup in self.power_ups_list:
            if check_for_collision(self.player_sprite, powerup):
                if powerup.properties['type'] == "Shotgun":
                    self.powerup = 1
                    self.powerupTimer = constants.POWER_UP_TIMER
                if powerup.properties['type'] == "MachineGun":
                    self.powerup = 2
                    self.powerupTimer = constants.POWER_UP_TIMER
                if powerup.properties['type'] == "extraLife":
                    self.lives = self.lives + 1
                if powerup.properties['type'] == "invincible":
                    self.powerup = 3
                    self.powerupTimer = constants.POWER_UP_TIMER / 2
                powerup.remove_from_sprite_lists()

        self.powerUpCountdown()

    def powerUpCountdown(self):
        self.powerupTimer = self.powerupTimer - 1

        if self.powerupTimer == 0:
            self.powerup = 0

    def getBulletPositionAndDirection(self, bullet, rotation):

        bullet.center_y = self.player_sprite.center_y - 14
        if self.player_sprite.character_face_direction == constants.RIGHT_FACING:
            bullet.center_x = self.player_sprite.center_x + 35 #position of the bullet
            bullet.change_x = constants.BULLET_SPEED
        else:
            if self.powerup == 1 and self.player_sprite.character_face_direction == constants.RIGHT_FACING:
                bullet.center_x = self.player_sprite.center_x - 35
                bullet.change_x = -constants.BULLET_SPEED
            else:
                bullet.center_x = self.player_sprite.center_x - 35
                bullet.change_x = -constants.BULLET_SPEED
                bullet.angle = rotation

    def checkGameOver(self):
        if self.lives == 0:
            #go to game over screen
            game_view = GameOverView()
            game_view.setup(self.player_sprite)
            self.window.show_view(game_view)

    def shootMultipleBullets(self):
        if self.bullet_count > 0:
            rotation = 180
            if self.bullet_iterator == 0:

                bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
                self.getBulletPositionAndDirection(bullet, rotation)
                self.bullet_list.append(bullet)
                self.bullet_count = self.bullet_count - 1

            elif self.bullet_iterator % 6 == 0:

                bullet = arcade.Sprite("images/animated_characters/newbullet.png", constants.SPRITE_SCALING_LASER)
                self.getBulletPositionAndDirection(bullet, rotation)
                self.bullet_list.append(bullet)
                self.bullet_count = self.bullet_count - 1

            self.bullet_iterator = self.bullet_iterator + 1

        if self.bullet_iterator > 1000:
            self.bullet_iterator = 0
                

    def on_draw(self):

        arcade.start_render()
        self.backgrounds_list.draw()
        self.wall_list.draw() 
        self.background_list.draw()
        self.enemies_list.draw()
        self.flag_list.draw()
        self.power_ups_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_bullet_list.draw()
       

         # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        life_text = f"Lives: {self.lives}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)
        arcade.draw_text(life_text, 150 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

#Views section

class GameWinView(arcade.View):
    """ View to show instructions """

    def setup(self, score, player):
        self.score = score
        self.center_x = player.center_x

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("You Win! Congratulations!", #self.center_x
                                                        constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Your score was " + str(self.score) + "!", self.center_x, constants.SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = FirstView()
        self.window.show_view(game_view)

class FirstView(arcade.View):
    """ View to show instructions """

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Game Title", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press any key to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = InstructionView()
        self.window.show_view(game_view)

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("images/tiles/gameover.png")
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def setup(self, player):
        self.center_x = player.center_x

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_HEIGHT / 2, constants.SCREEN_HEIGHT / 2 - 100,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_key_press(self, key, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = FirstView()
        self.window.show_view(game_view)

class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Instructions", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT /1.2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press the arrow keys to move. Press Space to shoot. \n\n Collect Powerups and get to the end of the levels to win!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")                 
        arcade.draw_text("Press any key to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 4,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, start the game. """
        lives = 3
        if key == arcade.key.C:
            lives = 15
        score = 0
        game_view = MyGame()
        game_view.setup(game_view.level, lives, score)
        self.window.show_view(game_view)

class LevelView(arcade.View):
    """ View to show instructions """


    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def setup(self, level, lives, score, player):
        self.cur_level = level
        self.lives = lives
        self.score = score
        self.world = 1
        self.displayedLevel = level
        self.center_x = player.center_x
        self.center_y = player.center_y

    def genWorld(self):
        if self.cur_level > 5 and self.cur_level < 11:
            self.world = 2
            self.displayedLevel = self.cur_level - 5

        elif self.cur_level >= 11:
            self.world = 3
            self.displayedLevel = self.cur_level - 10

    def on_draw(self):
        """ Draw this view """
        self.genWorld()
        textPhrase = "World " + str(self.world) + " - " + str(self.displayedLevel)
        livesPhrase = "Lives Remaining: " + str(self.lives)
        arcade.start_render()
        arcade.draw_text(textPhrase, self.center_x, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(livesPhrase, self.center_x, constants.SCREEN_HEIGHT / 2.5 ,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = MyGame()
        game_view.setup(self.cur_level, self.lives, self.score)
        self.window.show_view(game_view)