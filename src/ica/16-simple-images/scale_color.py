from PIL.ImageColor import getcolor

from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import Picture

def weighted_scale(pic, w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        r, g, b = new_pic.getColor(x, y)
        lumin = w1*r + w2*g + w3*b
        new_pic.setColor(x, y, (lumin, lumin, lumin))
    return new_pic

img = Picture("../SampleImages/mushrooms.jpg")
scaled = weighted_scale(img, 0.7, 0.2, 0.1)
scaled.show()
keep_windows_open()
