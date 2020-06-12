import cv2
import math
import cmath
import numpy as np
import sys
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def division(f2,f1,_min,_max,newMin,newMax):
    I = f2/f1
    #print(_max)
    valor = (I-_min)*((newMax-newMin)/(_max -_min))+newMin
    #valor = (f2/f1) * x
    if(valor>255):
        return 255
    if(valor<0):
        return 0
    return valor
def max_min(f1,f2):
    max=0
    min=255
    valor=0
    for i in range(0,row):
        for j in range(0,cols):
            valor = f1[i][j][0]/f2[i][j][0]
            if(valor>max):
                max = valor
            if(valor<min):
                min = valor
    return min,max


def main(filename,filename1):
    img1= cv2.imread(filename)
    img2= cv2.imread(filename1)

    row, cols ,channels = img1.shape
    img = cv2.resize(img2,(int(cols),int(row)))

    newMax = 255
    newMin = 0
    const = 170
    xmin = (img1[..., 0]/img[..., 0]).min()
    xmax = (img1[..., 0]/img[..., 0]).max()

    for i in range(0,row    ):
        for j in range(0,cols):
            img[i][j][0] = division(img1[i][j][0],img[i][j][0],xmin,xmax,newMin,newMax)
            img[i][j][1] = division(img1[i][j][1],img[i][j][1],xmin,xmax,newMin,newMax)
            img[i][j][2] = division(img1[i][j][2],img[i][j][2],xmin,xmax,newMin,newMax)

    strr = "uploads/solution_"+str(random.random())+".jpg"
    cv2.imwrite(strr,img)
    return strr


filename = sys.argv[1]
filename1 = sys.argv[2]
print(main(filename,filename1))

