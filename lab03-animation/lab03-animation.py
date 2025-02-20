import arcade
from arcade.color import BLACK

WIDTH = 800
HEIGHT = 600

def draw_sun():

    arcade.draw_line(425, 200, 1000, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 950, 950, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 900, 900, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(425, 200, 850, 850, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(375, 200, -200, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -150, 950, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -100, 900, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(375, 200, -50, 850, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 200, 400, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 200, 415, 1000, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 200, 385, 1000, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 180, 1000, 370, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, 1000, 360, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, 1000, 350, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_line(400, 180, -200, 370, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, -200, 360, arcade.color.SELECTIVE_YELLOW, 10)
    arcade.draw_line(400, 180, -200, 350, arcade.color.SELECTIVE_YELLOW, 10)

    arcade.draw_circle_filled(400, 200, 100, arcade.color.ORANGE_PEEL)
    arcade.draw_circle_filled(400, 200, 90, arcade.color.SELECTIVE_YELLOW)

def draw_ocean():
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.SPACE_CADET)

def draw_clouds():
    arcade.draw_ellipse_filled(200, 490, 300, 100, arcade.color.LIGHT_PINK, 0)
    arcade.draw_circle_filled(120, 485, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(170, 485, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(230, 495, 55, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(280, 490, 55, arcade.color.LIGHT_PINK)

    arcade.draw_ellipse_filled(200, 490, 290, 90, arcade.color.PINK_LACE, 0)
    arcade.draw_circle_filled(120, 485, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(170, 485, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(230, 495, 50, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(280, 490, 50, arcade.color.PINK_LACE)

    arcade.draw_ellipse_filled(700, 450, 310, 110, arcade.color.LIGHT_PINK, 0)
    arcade.draw_circle_filled(620, 455, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(670, 445, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(730, 455, 60, arcade.color.LIGHT_PINK)
    arcade.draw_circle_filled(780, 445, 60, arcade.color.LIGHT_PINK)

    arcade.draw_ellipse_filled(700, 450, 300, 100, arcade.color.PINK_LACE, 0)
    arcade.draw_circle_filled(620, 455, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(670, 445, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(730, 455, 55, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(780, 445, 55, arcade.color.PINK_LACE)

def draw_boat(x):
    arcade.draw_ellipse_filled(x, 110, 300, 150, arcade.color.DARK_JUNGLE_GREEN  , 0)
def draw_stick(x):
    arcade.draw_line(x, 90, x, 300, arcade.color.DARK_JUNGLE_GREEN, 5)
    arcade.draw_line(x - 100, 150, x + 100, 150, arcade.color.DARK_JUNGLE_GREEN, 5)

def draw_water_boat(x):
    arcade.draw_rectangle_filled(x, 150, 300, 90, arcade.color.SPACE_CADET)

def draw_waves(x):
    arcade.draw_ellipse_filled(x, -20, 300, 150, arcade.color.SPACE_CADET, 0)
    arcade.draw_ellipse_filled(x + 100, -20, 300, 150, arcade.color.SPACE_CADET, 0)
    arcade.draw_ellipse_filled(x + 220, -20, 300, 150, arcade.color.SPACE_CADET, 0)

def draw_sail(x):
    arcade.draw_triangle_filled(496 - x, 155, 402 - x, 155, 496 - x, 300, arcade.color.WHITE)
    arcade.draw_triangle_filled(503 - x, 155, 600 - x, 155, 503 - x, 300, arcade.color.WHITE)

    # Bird function
def draw_bird(x, y, z):
    arcade.draw_arc_outline(x, y, 50, z, arcade.color.BLACK, 0, 110, 4)
    arcade.draw_arc_outline(x + 50, y, 50, z, arcade.color.BLACK, 70, 180, 4)

def on_draw(delta_time):
    arcade.start_render()

    draw_sun()
    draw_ocean()
    draw_clouds()
    draw_bird(on_draw.bird_x, 500, on_draw.bird_wing)
    draw_bird(on_draw.bird_x + 300, 450, on_draw.bird_wing)
    draw_bird(on_draw.bird_x - 100, 280, on_draw.bird_wing)
    draw_bird(on_draw.bird_x + 440, 550, on_draw.bird_wing)
    on_draw.bird_x += 1.2
    draw_boat(on_draw.boat_x)
    if on_draw.bird_wing <= -10:
        on_draw.bird_wing = 50
    on_draw.bird_wing -= 1.5
    on_draw.boat_x -= 0.5
    draw_water_boat(on_draw.rect_x)
    on_draw.rect_x -= 0.5
    draw_stick(on_draw.stick_x)
    on_draw.stick_x -= 0.5
    draw_sail(on_draw.sail1_x)
    on_draw.sail1_x -= -0.5
    draw_waves(700)
    draw_waves(500)
    draw_waves(400)
    draw_waves(150)
    draw_waves(50)


on_draw.boat_x = 500
on_draw.rect_x = 500
on_draw.stick_x = 500
on_draw.sail1_x = -0.5
on_draw.bird_wing = 50
on_draw.bird_x = 200

def main():
    arcade.open_window(800, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.SINOPIA)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()