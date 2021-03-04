import arcade
import constants
from MyGame import MyGame

def main():
    window = MyGame()
    window.setup(window.level)
    arcade.run()

if __name__ == "__main__":
    main()