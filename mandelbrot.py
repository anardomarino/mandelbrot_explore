#!/usr/bin/python3

from PIL import Image
from numpy import complex, array
import colorsys
import sys

DEBUG = False

COLOR_SETTING = 75

WIDTH = 1920
HEIGHT = 1080
SIZE_FACTOR = 1
X_SHIFT = 0
Y_SHIFT = 0
ZOOM_FACTOR = 500
ITERATIONS = 1000
name = sys.argv[1]

def rgb_conv(i):
    color = 255*array(colorsys.hsv_to_rgb(i/COLOR_SETTING,1,0.5))
    return tuple(color.astype(int))

def mandelbrot(x,y):
    c0 = complex(x,y)
    c = 0
    for i in range(1, ITERATIONS):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c*c + c0
    return (0,0,0)

img = Image.new('RGB', (int(SIZE_FACTOR*WIDTH), int(SIZE_FACTOR*HEIGHT)))
pixels = img.load()

counter = 0
total = SIZE_FACTOR**2*WIDTH*HEIGHT
for x in range(-img.size[0]//2,img.size[0]//2):
    print("%.2f %%                      " % (counter/total*100), end='')
    print("\r",end='')
    for y in range(-img.size[1]//2,img.size[1]//2):
        if (x == 0 or y == 0) and DEBUG:
            counter += 1
            pixels[img.size[0]//2,img.size[1]//2] = (255,255,255)
            continue
        counter += 1
        pixels[x+img.size[0]//2,y+img.size[1]//2] = mandelbrot((x)/(ZOOM_FACTOR)-X_SHIFT,
                                                               (y)/(ZOOM_FACTOR)-Y_SHIFT)

img.save(name + ".jpg")
img.show()
