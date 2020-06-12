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
    valor = f1*c
    if(valor>255):
        return 255
    if(valor<0):
        return 0
    return valor

def main(filename,filename1):
    img1= cv2.imread(filename)
    row, cols ,channels = img1.shape
    img = img1.copy()
    c=filename1
    for i in range(0,row):
        for j in range(0,cols):
            img[i][j][0] = add_constant(img1[i][j][0],c)
            img[i][j][1] = add_constant(img1[i][j][1],c)
            img[i][j][2] = add_constant(img1[i][j][2],c)

    strr = "uploads/solution_"+str(random.random())+".jpg"
    cv2.imwrite(strr,img)
    return strr



filename = sys.argv[1]
filename1 = float(sys.argv[2])
print(main(filename,filename1))


