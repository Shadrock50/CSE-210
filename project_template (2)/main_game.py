import arcade
import constants
from MyGame import MyGame

def main():
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    startView = MyGame()
    window.show_view(startView)
    startView.setup(constants.START_LEVEL)
    arcade.run()

if __name__ == "__main__":
    main()