import arcade
import random
import time
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "STARS!!!!"
STAR_COUNT = 200  # Initial number of stars
REVOLUTION_CENTER_X = SCREEN_WIDTH // 2
REVOLUTION_CENTER_Y = SCREEN_HEIGHT // 2
REVOLUTION_SPEED_SLOW = 0.0001  # Slow speed of revolution in radians per update
REVOLUTION_SPEED_FAST = 0.05  # Extremely fast speed of revolution in radians per update
RADIUS_INCREMENT = 5.2  # Speed at which stars move outward
SIZE_INCREMENT = 0.07  # Speed at which stars grow
NEW_STAR_INTERVAL = 0.0001  # Interval in seconds to add new stars
UPDATE_TIME = 2  # Time in seconds until variables are updated

class Star:
    def __init__(self, x, y, size, brightness, angle, radius):
        self.x = x
        self.y = y
        self.size = size
        self.brightness = brightness
        self.angle = angle
        self.radius = radius

    def update_position(self, speed):
        self.x = REVOLUTION_CENTER_X + self.radius * math.cos(self.angle)
        self.y = REVOLUTION_CENTER_Y + self.radius * math.sin(self.angle)
        self.angle += speed
        self.radius += RADIUS_INCREMENT  # Increase the radius faster
        self.size += SIZE_INCREMENT # Increase the size slower

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.brightness)

class ShootingStar:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.size = random.uniform(2, 4)
        self.speed_x = random.uniform(-10, 10)
        self.speed_y = random.uniform(-10, 10)
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
        self.start_time = time.time()
        self.last_shooting_star_time = time.time()
        self.last_star_spawn_time = time.time()
        self.slow_down = False
        self.variables_changed = False

    def setup(self):
        # Create initial list of stars with varying sizes and brightness
        for _ in range(STAR_COUNT):
            self.spawn_star()

    def spawn_star(self):
        star_x = REVOLUTION_CENTER_X
        star_y = REVOLUTION_CENTER_Y
        star_size = random.uniform(1, 3)  # Star size between 1 and 3
        alpha = random.randint(128, 255)  # Vary brightness
        star_brightness = (255, 255, 255, alpha)  # RGB with Alpha
        angle = random.uniform(0, 2 * math.pi)  # Random initial angle
        radius = 0  # Start at the center
        star = Star(star_x, star_y, star_size, star_brightness, angle, radius)
        self.star_list.append(star)

    def on_draw(self):
        self.clear()
        # Draw stars
        for star in self.star_list:
            star.draw()

        # Draw shooting stars
        # for shooting_star in self.shooting_star_list:
        #     shooting_star.draw()

    def update_variables(self):
        global NEW_STAR_INTERVAL, SIZE_INCREMENT, RADIUS_INCREMENT, REVOLUTION_SPEED_FAST
        NEW_STAR_INTERVAL = 0.5
        SIZE_INCREMENT = 0.005
        RADIUS_INCREMENT = 0.2
        REVOLUTION_SPEED_FAST = 0.0001

    def on_update(self, delta_time):
        # Determine speed based on whether any stars have hit the edge
        speed = REVOLUTION_SPEED_FAST
        if not self.slow_down:
            for star in self.star_list:
                if (star.x + star.size < 0 or star.x - star.size > SCREEN_WIDTH or
                    star.y + star.size < 0 or star.y - star.size > SCREEN_HEIGHT):
                    self.slow_down = True
                    break
        if self.slow_down:
            speed = REVOLUTION_SPEED_SLOW

        # Update normal stars' positions
        for star in self.star_list:
            star.update_position(speed)

        # Remove stars that have moved fully off screen
        self.star_list = [
            star for star in self.star_list
            if not (star.x + star.size < 0 or star.x - star.size > SCREEN_WIDTH or
                    star.y + star.size < 0 or star.y - star.size > SCREEN_HEIGHT)
        ]

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
            if not (shooting_star.x + shooting_star.size < 0 or shooting_star.x - shooting_star.size > SCREEN_WIDTH or
                    shooting_star.y + shooting_star.size < 0 or shooting_star.y - shooting_star.size > SCREEN_HEIGHT)
        ]

        # Spawn new stars at the center of the vortex
        if current_time - self.last_star_spawn_time > NEW_STAR_INTERVAL:
            self.spawn_star()
            self.last_star_spawn_time = current_time

        # Update variables after the specified time
        if current_time - self.start_time > UPDATE_TIME and not self.variables_changed:
            self.update_variables()
            self.variables_changed = True

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()