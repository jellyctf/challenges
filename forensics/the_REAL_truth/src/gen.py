#!/usr/bin/env python3
from PIL import Image

im = Image.open("jellytruth.png")
pix = im.load()
width, height = im.size

flag = "jellyCTF{th3_w0man_in_th3_r3d_ch4nn3l}"
yap = "hello starknight. it is good to see you again. that you might uncover the truth from this image bodes well. however, do not grow complacent - for this is just the beginning of our journey together. further challenges await, and i shall be there. the time has come for us to part, but before we are separated, take this: "
# add some yap to make the modification more visible
text = yap + flag + "".join(reversed(yap)) * 5

count = 0
for h in range(height):
    for w in range(width):
        if count == len(text):
            break
        pix[w,h] = (
            ord(text[count]), # red
            pix[w,h][1], # green
            pix[w,h][2], # blue
            # pix[w,h][1] - ord(text[count]), # green
            # pix[w,h][2] - ord(text[count]), # blue
        )
        count += 1

im.save("chal.png")

# carrd is a bastard and will resample your shit to jpg even if it's under the
# size of a vector png that doesn't get resampled when uploading (100k or so).
# they probably convert your upload to jpg and png in parallel and pick the
# smallest one. since our image has a lot of noise (which we need to preserve),
# we can intercept the request to /publish in burp and paste from file our
# original images, while changing the mimetype to png, which it seems to accept
# just fine. they still seem to do some sort of compression (the images aren't
# identical), but the challenges still work due to the pixels not being modified
