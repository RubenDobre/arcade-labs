import random
import arcade
import math

CHARACTER_SCALING = 0.3
COIN_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def on_update(self, **kwargs):

        """ Update the ball's position.
        """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

    def update(self):
        self.on_update()

class BadCoin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def on_update(self, **kwargs):
        """ Update the ball's position.
        """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

    def update(self):
        self.on_update()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.bad_coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 5

        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(20):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("coin_01.png", COIN_SCALING / 3)

            # Position the center of the circle the coin will orbit
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            coin.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(30):

            bad_coin = BadCoin("coin_02.png", COIN_SCALING / 3)

            # Position the center of the circle the coin will orbit
            bad_coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            bad_coin.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            bad_coin.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.bad_coin_list.append(bad_coin)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()
        self.bad_coin_list.draw()

        # Put the text on the screen.

        if self.score <= 0:

            output = "¡GAME OVER!"
            arcade.draw_text(output, 200, 300, arcade.color.WHITE, 50)
        else:
            output = "Score: " + str(self.score)
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.score > 0:
            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.coin_list.update()
            self.bad_coin_list.update()

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.coin_list)

            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.bad_coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in hit_list:
                self.score += 1
                coin.remove_from_sprite_lists()

            for bad_coin in bad_hit_list:
                self.score -= 1
                bad_coin.remove_from_sprite_lists()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()