import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys
import random

def addition(img, img1):
    strimg= img
    img = cv2.imread(img)
    nimg1 = cv2.imread(img1)
    height, width, depth = img.shape
    img1 = cv2.resize(nimg1,(int(width),int(height)))
    img = np.uint8(img/2) + np.uint8(img1/2)
    strr = "uploads/solution_"+str(random.random())+".jpg"
    cv2.imwrite(strr,img)
    return strr
    
filename = sys.argv[1]
filename1 = sys.argv[2]
print(addition(filename,filename1))
