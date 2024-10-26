import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((10, 10, 25))
        self.i = 1

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        # Draw gradient sky
        for i in range(SCREEN_HEIGHT):
            arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT-i, SCREEN_HEIGHT-(i+1), (10, 10, 25+i//3))

        if self.i == 1:
            self.xp = []
            self.yp = []
            self.wave_positions = []

            # Generate star positions
            for _ in range(100):
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                self.xp.append(x)
                self.yp.append(y)

            # Generate wave positions
            for _ in range(10):
                start = random.randint(0, SCREEN_WIDTH-50)
                end = start + 30
                height = random.randint(150, 300)
                self.wave_positions.append((start, end, height))

            self.i = 0

        # Draw stars
        for i in range(100):
            x = self.xp[i]
            y = self.yp[i]
            arcade.draw_point(x, y, arcade.color.WHITE, 2)

        # Draw sun
        arcade.draw_circle_filled(400, 300, 70, (252, 219, 3))
        arcade.draw_circle_outline(400, 300, 70, (0, 0, 0))

        # Draw ocean
        for i in range(100):
            arcade.draw_lrtb_rectangle_filled(0, 800, 300-i*3, 0, (22, 33+i*2, 242))

        # Draw horizon
        arcade.draw_lrtb_rectangle_filled(0, 800, 301, 299, (0, 0, 0))

        # Draw waves
        for start, end, height in self.wave_positions:
            arcade.draw_lrtb_rectangle_filled(start, end, height, height-1, (255, 255, 255))

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
