# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:43:05 2023

    Dans le grand type de ce type il saffit

@author: Ali
"""

from PIL import Image, ImageDraw, ImageFont
import os,glob
import numpy as np
import random
from pathlib import Path as pathFile

parentPath = "C:/Users/Ali/Desktop/PhD data/OCR tifinagh/dataset_tifinagh"

charactersList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

fontTypes=[]


for font in glob.glob("C:/Users/Ali/Desktop/PhD data/generate/tifin/*"): # Create Image for every font
    fontTypes.append(os.path.abspath(font))
    
for index,character in enumerate(charactersList):    
    path = os.path.join(parentPath, str(index))

    if not os.path.exists(path):
        os.mkdir(path)

        
    for imageCounter in range(len(fontTypes)):
        for repeats in range(1): # Number of Images
            fnt = ImageFont.truetype(fontTypes[imageCounter], random.randint(42, 42))
            w, h = fnt.getsize(character)
            img_w, img_h = 64, 64  # Add 60 pixels padding (assume 10 pixels from each side).
            img = Image.new('L', (img_w, img_h), color='black')  # Replace '1' with 'L' (8-bit pixels, black and white - we fill 255 so we can't use 1 bit per pixel)
            d = ImageDraw.Draw(img)
            d.text(((img_w-w)/2, (img_h-h)/2), character, font=fnt, fill=255, align="center") # TO ALIGN CHARACTER IN CENTER
            img.save(path+"\\"+str(imageCounter)+"_"+str(repeats)+".jpg")