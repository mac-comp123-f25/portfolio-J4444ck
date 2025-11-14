from src.ica.helpers.imageTools import Picture
from src.ica.helpers.dummyWindow import keep_windows_open

def crop_picture(src_pic, start_x, start_y, crop_width, crop_height):
    new_pic = Picture(crop_width, crop_height)


    for x in range(crop_width):
        for y in range(crop_height):
            src_x = start_x + x
            src_y = start_y + y

            color = src_pic.getColor(src_x, src_y)
            new_pic.setColor(x, y, color)

    return new_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()
keep_windows_open()