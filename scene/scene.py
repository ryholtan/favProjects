# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Tatooine", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    
    #draw ground 
    draw_ground(canvas, scene_width, scene_height)
    
    # give user option to change the scenery a little
    storm = input("Is it stormy?(y/n) ").lower()
    # make it rain
    if storm == "y":
        precipitation = input("How stormy is it?(1. light, 2. moderate, 3. heavy, 4. cats and dogs) ").lower()
        if precipitation == "1":
            draw_raindrop(canvas, scene_width, scene_height)
        elif precipitation == "2":
            draw_raindrop(canvas, scene_width, scene_height, "moderate")
        elif precipitation == "3":
            draw_raindrop(canvas, scene_width, scene_height, "heavy")
        elif precipitation == "4":
            draw_raindrop(canvas, scene_width, scene_height, "cats_dogs")


    # draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)



# Define your functions such as
# draw_sky and draw_ground here.
def draw_lightning(canvas, width, height):
    """call the power of zeus to your aid!
    pass in canvas, width, and height to get a 
    random yellow streak across the top 2/3
    of your scene"""

    light_length = random.randrange(round(height / 3), height)
    light_x = random.randrange(3, width)
    light_x2 = random.randrange(3, width)
    light_y = random.randrange(round(height / 5), height)
    draw_line(canvas, light_x, light_y, light_x2, light_y + light_length, width=3, fill="yellow1")


def draw_raindrop(canvas, width, height, precipitation="light"):
    """draw rain drops all over screen
    pass canvas, width and height of screen, and precipitation amount
    (light, moderate, heavy, cats_dogs) if precipitation = heavy or cats_dogs
    clouds become more prevelant and darker along with an addition of lightning"""

    if precipitation == "light":
        interval = width / 25
    elif precipitation == "moderate":
        interval = width / 50
    elif precipitation == "heavy":
        interval = width / 100
        # draw storm clouds 
        for i in range(0, 800, 100):
            diameter = random.randrange(100, width)
            draw_clouds(canvas, random.randrange(0, width), random.randrange(350, height), diameter)
    elif precipitation == "cats_dogs":
        interval = width / 500
        # draw storm clouds
        # and lightning 
        for i in range(0, 800, 100):
            # call draw lightning
            draw_lightning(canvas, width, height)
            diameter = random.randrange(100, width)
            draw_clouds(canvas, random.randrange(0, width), random.randrange(350, height), diameter)

    # draw every x drop
    for x in range(round(interval), width, round(interval)):
        ran_x = random.randrange(1, width)
        ran_y = random.randrange(1, height)
        draw_line(canvas, ran_x, ran_y, ran_x, ran_y + 3, fill="blue3")
    
    # draw every y drop
    for y in range(round(interval), width, round(interval)):
        ran_x = random.randrange(1, width)
        ran_y = random.randrange(1, height)
        draw_line(canvas, ran_x, ran_y, ran_x, ran_y + 3, fill="blue3")


def draw_clouds(canvas, center_x, center_y, size):
    """draw long sandy cloud
    pass in canvas, left and bottom coordinates, and
    size to grow cloud, if size is >=500, cloud is 
    darker"""
    
    right_x = center_x + size
    bottom_y = center_y - size / 15
    # draw big dark cloud
    if size >= 500:
        draw_oval(canvas, center_x, center_y, right_x, bottom_y, fill="gray31")
    else:
        draw_oval(canvas, center_x, center_y, right_x, bottom_y, fill="mistyRose4")

def draw_Grogu(canvas, center_x, center_y, size):
    """Draw a floating "carriage" with Grogu in it, pass canvas, leftmost x cor, bottommost y cor, and his size(size doesn't work yet."""

    # """float thingy Grogu rides in"""
    # backdrop circle
    outer_x = size / 2 + center_x
    outer_y = size / 2 + center_y
    draw_oval(canvas, center_x, center_y, outer_x, outer_y, width=2, outline="black", fill="gray60")

    # rectangle belt thing
    _left = center_x 
    _right = outer_x
    _down = center_y + size / 5
    _up = center_y + size / 5 + 10
    draw_rectangle(canvas, _left, _down, _right, _up, width=2, fill="gray49")

    # """Grogu and clothes"""
    # scarfs
    # top scarf
    scarf_center_x = center_x + round(size / 8)
    scarf_center_y = center_y + round(size / 3.255)
    scarf_size_x = (size / 4) + scarf_center_x
    scarf_size_y = scarf_center_y - (size / 25) 
    draw_oval(canvas, scarf_center_x, scarf_center_y, scarf_size_x, scarf_size_y, fill="wheat")
    # bottom scarf
    # scarf_center_x = center_x + round(size / 8)
    # scarf_center_y = center_y + round(size / 3.255)
    # scarf_size_x = (size / 4) + scarf_center_x
    # scarf_size_y = scarf_center_y - (size / 25)
    draw_oval(canvas, 620, 220, 710, 210, fill="wheat")
    """Finish Grogu so he can be placed closer or further from the screen by scaling his size
    do the same whith "huts" and thier water collectors"""
    # ears
    draw_polygon(canvas, 642, 235, 625, 250, 650, 248, fill="paleGreen4")
    draw_polygon(canvas, 685, 235, 702, 250, 677, 248, fill="paleGreen4")

    # head oval
    draw_oval(canvas, 640, 250, 690, 226, fill="paleGreen4")
    # eyes 
    draw_oval(canvas, 650, 235, 660, 245, fill="black")
    draw_oval(canvas, 670, 235, 680, 245, fill="black")


def draw_sun(canvas, center_x, center_y, size):
    outer_x = center_x + size / 2
    outer_y = center_y + size / 2
    draw_oval(canvas, center_x, center_y, outer_x, outer_y, fill="firebrick4" )

def draw_hill(canvas, center, hill_bottom, hill_height):
    hill_top = hill_bottom + hill_height
    hill_right = center + hill_height
    hill_left = center - hill_height
    draw_polygon(canvas, center, hill_top, hill_right, hill_bottom, hill_left, hill_bottom, outline="tan4", fill="darkOrange4")

def draw_ground(canvas, width, height):
    draw_rectangle(canvas, 0, 0, width, 289, fill="tan4")
    
    # draw many hills
    for x in range(85, 725, 100):
        # draw a hill
        draw_hill(canvas, x, random.randrange(71, 287), random.randrange(25, 80))

    # draw our little friend
    draw_Grogu(canvas, 600, 150, 250)

def draw_sky(canvas, width, height):
    draw_rectangle(canvas, 0, 290, width, height, fill="burlywood2")
    
    # draw suns
    for i in range(0, 800, 600):
        diameter = random.randrange(50, 500)
        draw_sun(canvas, random.randrange(0, width), random.randrange(275, height), diameter)
    # draw clouds
    for i in range(0, 800, 100):
        diameter = random.randrange(20, 300)
        draw_clouds(canvas, random.randrange(0, width), random.randrange(350, height), diameter)


def draw_grid(canvas, width, height, interval):
    # draw vertical lines
    y_space = 20
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, y_space, (f"{x}"))

    #draw horizontal lines
    x_space = 20
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, x_space, y, (f"{y}"))



# Call the main function so that
# this program will start executing.
main()