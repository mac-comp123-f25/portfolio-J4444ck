import random

def copy_pic_random(small_pic, big_pic):
    big_w   = big_pic.getWidth()
    big_h   = big_pic.getHeight()
    small_w = small_pic.getWidth()
    small_h = small_pic.getHeight()

    start_x = random.randrange(big_w - small_w + 1)
    start_y = random.randrange(big_h - small_h + 1)

    for x in range(small_w):
        for y in range(small_h):
            color = small_pic.getColor(x, y)
            big_pic.setColor(start_x + x, start_y + y, color)

    return big_pic
