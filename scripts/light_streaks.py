#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:43:40 2019

@author: raymondmg
"""

import cv2
import numpy as np


image_path = "../images/demo1.png"
img = cv2.imread(image_path)
img_c = img.copy()
h,w,c = img.shape
out = np.zeros((h,w,c))
out_c = np.zeros((h,w,c))

#demo2 0.905
a = 0.925

pix_num = 64

for d in range(4):
    theta = 2 * np.pi/4 * d + np.pi/4
    _dir = [np.cos(theta), np.sin(theta)]
    
    _offsetx = np.zeros(pix_num)
    _offsety = np.zeros(pix_num)
    _w = np.zeros(pix_num)
    
    for p in range(3):
        sum_w = 0
        for s in range(pix_num):
            b = np.power(4,p)
            _offsetx[s] = int(_dir[0] * (b * s))
            _offsety[s] = int(_dir[1] * (b * s))
            _w[s] = np.power(a, (b * s)) 
            sum_w += _w[s]
        for j in range(h):
            for i in range(w):
                valb = 0
                valg = 0
                valr = 0
                for ofst in range(pix_num):
                    nj = int(j + _offsety[ofst])
                    ni = int(i + _offsetx[ofst])
                    if nj >= h or ni>= w or nj<0 or ni<0:
                        continue
                    valb+= _w[ofst]/sum_w * img[nj,ni,0]
                    valg+= _w[ofst]/sum_w * img[nj,ni,1]
                    valr+= _w[ofst]/sum_w * img[nj,ni,2]
                out[j,i,0] = valb 
                out[j,i,1] = valg 
                out[j,i,2] = valr 
                
                out_c[j,i,0] += out[j,i,0] 
                out_c[j,i,1] += out[j,i,1] 
                out_c[j,i,2] += out[j,i,2] 
        img = out     
    #out_c += img
    img = img_c
cv2.imwrite("../images/out1.png",out_c)