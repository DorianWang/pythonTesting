
from Cimpl import *


def build_hot_metal_lookup_table():
    table = [0]*256
    for i in range(0, 256):
        table[i] = create_color(min(255, i/170*255), 
                                max(0, i/85*255-510), 
                                0)
    return table

hot_metal_table = build_hot_metal_lookup_table()


def hot_metal(img, table):

    for x, y, col in img:
        red, green, blue = col
        weighted_brightness = 0.3 * red + 0.59 * green + 0.11 * blue
        set_color(img, x, y, table[int(weighted_brightness + 0.1)])


