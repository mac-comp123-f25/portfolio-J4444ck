from PIL.ImageColor import getcolor

from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import Picture

def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for x in range(small_pic.getWidth()):
        for y in range(small_pic.getHeight()):
            color = small_pic.getColor(x, y)

            big_x = start_x + x
            big_y = start_y + y

            big_pic.setColor(big_x, big_y, color)


green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()
keep_windows_open()
