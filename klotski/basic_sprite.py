import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)
    
    def on_draw(self):
        arcade.start_render()


def main():
    windows = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()