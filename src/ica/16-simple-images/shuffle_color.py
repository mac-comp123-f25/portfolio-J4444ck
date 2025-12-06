from PIL.ImageColor import getcolor

from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import Picture

def color_shuffle(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        r, g, b = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (g, b, r))
    return new_pic

mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
mushrooms1 = color_shuffle(mushrooms0)
mushrooms2 = color_shuffle(mushrooms1)

mushrooms0.show()
mushrooms1.show()
mushrooms2.show()
keep_windows_open()




