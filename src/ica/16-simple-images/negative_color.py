from PIL.ImageColor import getcolor

from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def negative(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        r, g, b = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (255-r, 255-g, 255-b))
    return new_pic

img = Picture("../SampleImages/mushrooms.jpg")
neg = negative(img)
neg.show()
keep_windows_open()
