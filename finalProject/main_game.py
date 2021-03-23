inimport arcade
import constants
from MyGame import FirstView

def main():
    
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = FirstView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()