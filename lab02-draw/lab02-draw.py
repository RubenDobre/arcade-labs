import arcade
from arcade.color import BLACK

WIDTH = 800
HEIGHT = 600

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.SINOPIA)

arcade.start_render()

# Drawing here

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

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.SPACE_CADET)

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

arcade.draw_ellipse_filled(500, 110, 300, 150, arcade.color.DARK_JUNGLE_GREEN  , 0)

arcade.draw_rectangle_filled(500, 150, 300, 90, arcade.color.SPACE_CADET)

arcade.draw_ellipse_filled(400, -20, 300, 150, arcade.color.SPACE_CADET, 0)
arcade.draw_ellipse_filled(500, -20, 300, 150, arcade.color.SPACE_CADET, 0)
arcade.draw_ellipse_filled(620, -20, 300, 150, arcade.color.SPACE_CADET, 0)

arcade.draw_line(500, 90, 500, 300, arcade.color.DARK_JUNGLE_GREEN, 5)
arcade.draw_line(400, 150, 600, 150, arcade.color.DARK_JUNGLE_GREEN, 5)

arcade.draw_triangle_filled(496, 155, 402, 155, 496, 300, arcade.color.WHITE)
arcade.draw_triangle_filled(503, 155, 600, 155, 503, 300, arcade.color.WHITE)

#  End of render

arcade.finish_render()

arcade.run()