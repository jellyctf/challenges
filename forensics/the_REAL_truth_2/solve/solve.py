#!/usr/bin/env python3
from PIL import Image

# go to /robots.txt -> /sitemap.xml -> find image02.png

im = Image.open("image01.png")
im2 = Image.open("image02.png")
pix = im.load()
pix2 = im2.load()
width, height = im.size

for h in range(height):
    for w in range(width):
        if pix[w,h] != pix2[w,h]:
            print(pix[w,h], pix2[w,h])
            pix[w,h] = (255, 0, 0)

im.save("solve.png")

# or use stegsolve "Image Combiner" with XOR/SUB
