import arcade
import random
import math
import datetime 

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Star Explosion Animation"
EXPLOSION_INTERVAL = 1.0  # Time between starting new explosions in seconds

class StarExplosion(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.star_x = SCREEN_WIDTH // 2
        self.star_y = SCREEN_HEIGHT // 2
        self.star_radius = 5
        self.explosion_max_radius = 300
        self.explosion_speed = 2
        self.colors = [arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.BLUE, arcade.color.INDIGO, arcade.color.VIOLET]
        self.explosions = []  # List to hold all active explosions
        self.last_explosion_time = 0

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.draw_explosions()

    def update(self, delta_time):
        current_time = datetime.time
        if current_time - self.last_explosion_time >= EXPLOSION_INTERVAL:
            self.start_new_explosion()
            self.last_explosion_time = current_time

        # Update all explosions
        for explosion in self.explosions:
            explosion['radius'] += self.explosion_speed

        # Remove explosions that have reached their maximum radius
        self.explosions = [explosion for explosion in self.explosions if explosion['radius'] < self.explosion_max_radius]

    def start_new_explosion(self):
        explosion = {
            'x': self.star_x,
            'y': self.star_y,
            'radius': 0,
            'colors': [random.choice(self.colors) for _ in range(50)]
        }
        self.explosions.append(explosion)

    def draw_star(self, center_x, center_y, size, color):
        angle = math.pi / 2
        for i in range(5):
            x = center_x + size * math.cos(angle)
            y = center_y + size * math.sin(angle)
            arcade.draw_line(center_x, center_y, x, y, color, 2)
            angle += math.pi / 5

    def draw_explosions(self):
        num_fragments = 50
        for explosion in self.explosions:
            for i in range(num_fragments):
                angle = 2 * math.pi * i / num_fragments
                x = explosion['x'] + explosion['radius'] * math.cos(angle)
                y = explosion['y'] + explosion['radius'] * math.sin(angle)
                color = explosion['colors'][i]
                self.draw_star(x, y, self.star_radius, color)

def main():
    window = StarExplosion()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
