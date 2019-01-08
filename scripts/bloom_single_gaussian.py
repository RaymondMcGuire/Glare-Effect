# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:53:27 2018

@author: raymondmg
"""

import cv2
import numpy as np

image_path = "../images/"

def RGB2YUV(r,g,b):
    return 0.299 * r + 0.587 * g + 0.114* b

def BlurImage(im,amount):
    out = im.copy()
    for i in range(amount):
        out = cv2.GaussianBlur(out,(7,7),0)
    return out

def Blend(im,blur):
    height,width,channel = im.shape
    out = np.zeros((height,width,channel))
    for j in range(height):
        for i in range(width):
            for c in range(channel):
                out[j,i,c] = im[j,i,c]+blur[j,i,c]
    return out

im = cv2.imread(image_path+"in.png")
height,width,channel = im.shape
bright_image = np.zeros((height,width,channel))
for j in range(height):
    for i in range(width):
        bgr = im[j,i]
        brightness = RGB2YUV(bgr[2],bgr[1],bgr[0])
        bright_image[j,i] = (brightness,brightness,brightness)


cv2.imwrite(image_path+"bright.jpg",bright_image)

blur_image = BlurImage(bright_image,15)

cv2.imwrite(image_path+"blur_image.jpg",blur_image)

bloom_image = Blend(im,blur_image)

cv2.imwrite(image_path+"bloom_image.jpg",bloom_image)