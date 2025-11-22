from simpleimage import SimpleImage
import math

def scale_down(image):
    old_w = image.width
    old_h = image.height

    new_w = math.ceil(old_w / 2)
    new_h = math.ceil(old_h / 2)

    small = SimpleImage.blank(new_w, new_h)

    for y in range(new_h):
        for x in range(new_w):
            src_x = x * 2
            src_y = y * 2

            if src_x >= old_w:
                src_x = old_w - 1
            if src_y >= old_h:
                src_y = old_h - 1

            src_pixel = image.get_pixel(src_x, src_y)
            dst_pixel = small.get_pixel(x, y)

            dst_pixel.red = src_pixel.red
            dst_pixel.green = src_pixel.green
            dst_pixel.blue = src_pixel.blue

    return small