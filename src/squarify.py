#!/usr/bin/env python3

from PIL import Image

import argparse
import glob
import os
import sys

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

def glob_extns(path):
    images = []
    for ext in extensions:
        p = os.path.join(path, f"*.{ext}")
        images += glob.glob(p)
    
    return images

def main(directory, file):
    images = []
    if file is not None:
        for f in file:
            idx = f.rfind('.')
            if f[idx + 1:] not in extensions:
                print(f"{f} not a recognized format... ignoring")
                continue
            images.append(f)

    if directory is not None:
        images.append(glob_extns(directory))

    for im in images:
        idx = im.rfind('.') 
        output = f"{im[:idx]}_square{im[idx:]}"

        if 'square' in im:
            print(f"{im} already suqarified... skipping!")
            continue

        square_img(im, output)

def setup_argparse():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dir")
    parser.add_argument("-f", "--file", action="append")

    args = parser.parse_args()

    if not args.dir and not args.file:
        parser.error("No action supplied, please define --dir or --file")
        return None

    return args

if __name__ == "__main__":
    args = setup_argparse()

    if args is not None:
        main(args.dir, args.file)

