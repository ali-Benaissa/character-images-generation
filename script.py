1.	# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:06:45 2023

@author: Ali
"""

from PIL import Image, ImageDraw, ImageFont
import os
import glob
import random

# Define global paths
parentPath = "//path_to_save_data"
fontPath = "//path_of_fonts"

charactersList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Get list of font paths
fontTypes = glob.glob(fontPath)

# Define global path variable
path = None

def create_image(character, imageCounter, repeats):
    global path
    fnt = ImageFont.truetype(fontTypes[imageCounter], 42)  # Fixed font size to 42
    w, h = fnt.getsize(character)
    img_w, img_h = 64, 64  # Add 60 pixels padding (assume 10 pixels from each side).
    img = Image.new('L', (img_w, img_h), color='black')
    d = ImageDraw.Draw(img)
    d.text(((img_w - w) // 2, (img_h - h) // 2), character, font=fnt, fill=255, align="center")
    img.save(os.path.join(path, f"{imageCounter}_{repeats}.jpg"))

# Create images for each character
for index, character in enumerate(charactersList):
    path = os.path.join(parentPath, str(index))
    os.makedirs(path, exist_ok=True)

for imageCounter, _ in enumerate(fontTypes):
    for repeats in range(1):  # Number of Images
        create_image(character, imageCounter, repeats)
