"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
SCREEN_TITLE = "klotski"


class Block(arcade.SpriteSolidColor):

    def __init__(self, width, height, color, name):
        super().__init__(width, height, color)
        self.name = name

    
    def can_move(self, sprites: arcade.SpriteList) -> bool:
        flag = True
        

        pass


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.block_list = arcade.SpriteList(use_spatial_hash=True)
        self.player = None

        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        caocao = Block(200, 200, arcade.color.RED, "Cao Cao")
        caocao.center_x = 200
        caocao.center_y = 400
        self.block_list.append(caocao)

        zhangfei = Block(100, 200, arcade.color.AFRICAN_VIOLET, "Zhang Fei")
        zhangfei.center_x = 50
        zhangfei.center_y = 400
        self.block_list.append(zhangfei)

        huangzhong = Block(100, 200, arcade.color.AMARANTH_PURPLE, "Huang Zhong")
        huangzhong.center_x = 350
        huangzhong.center_y = 400
        self.block_list.append(huangzhong)

        zhaoyun = Block(100, 200, arcade.color.GREEN, "Zhao Yun")
        zhaoyun.center_x = 50
        zhaoyun.center_y = 200
        self.block_list.append(zhaoyun)

        machao = Block(100, 200, arcade.color.GREEN_YELLOW, "Ma Chao")
        machao.center_x = 350
        machao.center_y = 200
        self.block_list.append(machao)


        guanyu = Block(200, 100, arcade.color.RED_DEVIL, "Guan Yu")
        guanyu.center_x = 200
        guanyu.center_y = 250
        self.block_list.append(guanyu)

        for i in range(4):
            name = f"Soldier-{i}"
            soldier = Block(100, 100, (0, 50*i, 200+20*i), name)
            soldier.center_x = 50 + 100 * i
            soldier.center_y = 50
            self.block_list.append(soldier)
        
        for block in self.block_list:
            print(block.name)


    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here

        self.block_list.draw()





def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()