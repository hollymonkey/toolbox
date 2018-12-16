import os
import cv2
import sys
import numpy as np
from PIL import Image
 
path = r'/media/xiaoming/ming/env/dataset/ship_dataset/hsrc'
 
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.jpg':
        img = Image.open(path+"/"+filename)
        img.save(path + '/' +  filename)

