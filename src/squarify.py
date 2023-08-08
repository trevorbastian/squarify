#!/usr/bin/env python3

from PIL import Image
import os
import sys
import glob

extensions = ['jpg', 'jpeg', 'png']

def square_img(img, output):
    im = Image.open(img)
    w, h = im.size

    new_h = h if h > w else w
    bg = Image.new(mode='RGB', size=(new_h, new_h), color='white')

    x = 0
    y = 0
    if w != new_h:
        x = int((new_h - w) / 2.0)
    else:
        y = int((new_h - h) / 2.0)

    bg.paste(im, (x,y))
    bg.save(output, quality=100)

def glob_jpeg(path):
    images = []
    for ext in extensions:
        p = os.path.join(path, f"*.{ext}")
        images += glob.glob(p)
    
    return images

if __name__ == "__main__":
    path = '.'
    if len(sys.argv) == 2:
        path = sys.argv[1]

    images = glob_jpeg(path)
    for im in images:
        idx = im.rfind('.') 
        output = f"{im[:idx]}_square{im[idx:]}"

        if 'square' in im:
            print(f"{im} already suqarified... skipping!")
            continue

        square_img(im, output)

