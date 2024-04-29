#!/usr/bin/env python3
from PIL import Image

im = Image.open("chal.png")
pix = im.load()
width, height = im.size
pixel_values = list(im.getdata())

for pixel in pixel_values[:1000]:
    print(chr(pixel[0]), end='')

# or use stegsolve's "Data Extract" with all R bits set