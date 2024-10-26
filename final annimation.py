import arcade
import random
import time
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "High Quality Starry Sky with Revolving Stars and Shooting Stars"
STAR_COUNT = 200  # Number of stars
REVOLUTION_CENTER_X = SCREEN_WIDTH // 2
REVOLUTION_CENTER_Y = SCREEN_HEIGHT // 2
REVOLUTION_SPEED = 0.0005  # Speed of revolution in radians per update

class Star:
    def __init__(self, x, y, size, brightness, angle, radius):
        self.x = x
        self.y = y
        self.size = size
        self.brightness = brightness
        self.angle = angle
        self.radius = radius

    def update_position(self):
        self.x = REVOLUTION_CENTER_X + self.radius * math.cos(self.angle)
        self.y = REVOLUTION_CENTER_Y + self.radius * math.sin(self.angle)
        self.angle += REVOLUTION_SPEED

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.brightness)

class ShootingStar:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.size = random.uniform(2, 4)
        self.speed_x = random.uniform(-15, 20)
        self.speed_y = random.uniform(-15, 20)
        self.brightness = (255, 255, 255, 255)  # White with full alpha
        self.trail = []

    def update(self):
        self.trail.append((self.x, self.y, self.size, self.brightness))
        if len(self.trail) > 10:
            self.trail.pop(0)
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        for i, (trail_x, trail_y, trail_size, trail_brightness) in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            arcade.draw_circle_filled(trail_x, trail_y, trail_size, (*trail_brightness[:3], alpha))
        arcade.draw_circle_filled(self.x, self.y, self.size, self.brightness)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)
        self.star_list = []
        self.shooting_star_list = []
        self.last_shooting_star_time = time.time()

    def setup(self):
        # Create a list of stars with varying sizes and brightness
        for _ in range(STAR_COUNT):
            star_x = random.randint(0, SCREEN_WIDTH)
            star_y = random.randint(0, SCREEN_HEIGHT)  # Top 3/4 of the screen
            star_size = random.uniform(1, 3)  # Star size between 1 and 3
            alpha = random.randint(128, 255)  # Vary brightness
            star_brightness = (255, 255, 255, alpha)  # RGB with Alpha
            angle = random.uniform(0, 2 * math.pi)  # Random initial angle
            radius = math.hypot(star_x - REVOLUTION_CENTER_X, star_y - REVOLUTION_CENTER_Y)  # Distance from the center
            star = Star(star_x, star_y, star_size, star_brightness, angle, radius)
            self.star_list.append(star)

    def on_draw(self):
        self.clear()
        # Draw stars
        for star in self.star_list:
            star.draw()

        # Draw shooting stars
        for shooting_star in self.shooting_star_list:
            shooting_star.draw()

    def on_update(self, delta_time):
        # Update normal stars' positions
        for star in self.star_list:
            star.update_position()

        # Update shooting stars
        current_time = time.time()
        if current_time - self.last_shooting_star_time > random.uniform(2, 5):
            self.shooting_star_list.append(ShootingStar())
            self.last_shooting_star_time = current_time

        for shooting_star in self.shooting_star_list:
            shooting_star.update()

        # Remove shooting stars that have moved off screen
        self.shooting_star_list = [
            shooting_star for shooting_star in self.shooting_star_list
            if 0 <= shooting_star.x <= SCREEN_WIDTH and 0 <= shooting_star.y <= SCREEN_HEIGHT
        ]
        
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
