#!/usr/bin/env python3

from PIL import Image
import os

path = "/home/student-04-75161e485c3f/images/"
for file in os.listdir(path):
    if not file.startswith("."):
        im = Image.open(path + file).convert('RGB')
        im.rotate(-90).resize((128,128)).save("/opt/icons/" + file, "JPEG")
        im.close()

#conver, resize and rotate image

