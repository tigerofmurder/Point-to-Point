import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys
import random

def subtract(img, img1):
    img = cv2.imread(img)
    nimg1 = cv2.imread(img1)
    height, width, depth = img.shape
    img1 = cv2.resize(nimg1,(int(width),int(height)))
    for y in range(0,width):
    	for x in range(0,height):
    	    c1=int(img[x,y,0])-int(img1[x,y,0])
    	    c2=int(img[x,y,1])-int(img1[x,y,1])
    	    c3=int(img[x,y,2])-int(img1[x,y,2])
    	    if(c1<0 and c2<0 and c3<0):
    	        c1,c2,c3 = 0,0,0
    	    elif(c1>255 and c2>255 and c3>255):
    	        c1,c2,c3 = 255,255,255
    	    img[x,y,0] = c1
    	    img[x,y,1] = c2
    	    img[x,y,2] = c3
    
    strr = "uploads/solution_"+str(random.random())+".jpg"
    #img = cv2.subtract(img,img1)
    cv2.imwrite(strr,img)
    return strr
    
filename = sys.argv[1]
filename1 = sys.argv[2]
print(subtract(filename,filename1))
