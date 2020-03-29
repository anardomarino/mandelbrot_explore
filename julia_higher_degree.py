#!/usr/bin/python3

from PIL import Image
from numpy import complex, array
import colorsys
import sys

DEBUG = False

COLOR_SETTING = 75              # Controls color saturation. Raise for more monochromatic,
                                # lower for more colors.
# Image Ratio
WIDTH = 1920
HEIGHT = 1080
# Image Scale
SIZE_FACTOR = 1
# Linear shift of the image
X_SHIFT = 0                     # Raise to shift image to the right
Y_SHIFT = 0                     # Raise to shift image downwards
# Controls scale of the fractal
ZOOM_FACTOR = 500               # Increase to zoom in
# Controls generation of fine structures
ITERATIONS = 100               # Increase for more precise fractal
                                # generation. Will slow down process.
name = sys.argv[1]

def rgb_conv(i):
    color = 255*array(colorsys.hsv_to_rgb(i/COLOR_SETTING,1,0.5))
    return tuple(color.astype(int))

def julia(x,y):
    c = complex(x,y) # the c is the imaginary version of your coordinate
    c0 = complex(sys.argv[2]) # this is the constant you enter in the form of a+bj (note: no spaces and j, not i)
    n = int(sys.argv[3]) # the power you want your c to be raised to
    for i in range(1, ITERATIONS):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c**n + c0
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
        pixels[x+img.size[0]//2,y+img.size[1]//2] = julia((x)/(ZOOM_FACTOR)-X_SHIFT,
                                                               (y)/(ZOOM_FACTOR)-Y_SHIFT)

img.save(name + ".jpg")
img.show()