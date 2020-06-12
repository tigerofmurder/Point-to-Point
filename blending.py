import cv2
import math
import cmath
import numpy as np
import sys
import random

def Normal_adition(f1,f2):
    valor = f1/2 + f2/2
    if(valor>255):
        return 255
    if(valor<0):
        return 0
    return valor
def add_constant(f1,c):
    valor = f1 + c
    if(valor>255):
        return 255
    if(valor<0):
        return 0
    return valor

def Blending(x,f1,f2):
    valor = x * f1 + (1-x)*f2
    if(valor>255):
        return 255
    if(valor<0):
        return 0
    return valor

def main(filename,filename1,x):
    img1= cv2.imread(filename)
    img2= cv2.imread(filename1)
    
    row, cols ,channels = img1.shape
    img = cv2.resize(img2,(int(cols),int(row)))
    
    for i in range(0,row):
        for j in range(0,cols):
            img[i][j][0] = Blending(x,img1[i][j][0],img[i][j][0])
            img[i][j][1] = Blending(x,img1[i][j][1],img[i][j][1])
            img[i][j][2] = Blending(x,img1[i][j][2],img[i][j][2])
    strr = "uploads/solution_"+str(random.random())+".jpg"
    cv2.imwrite(strr,img)
    return strr


filename = sys.argv[1]
filename1 = sys.argv[2]
x = float(sys.argv[3])
print(main(filename,filename1,x))
