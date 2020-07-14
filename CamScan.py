import cv2
import numpy
import numpy as np
import math
import random
import sys
def Histo_Color(img):
    rows,cols,channels = img.shape
    total = rows*cols
    for c in range(channels):
        frec = [0] * 256
        hist,bins = np.histogram(img[:,:,c].ravel(),256,[0,256])
        hist = [round(x/total,5) for x in hist]
        for i in range(1,256):
            hist[i] = round((hist[i]+hist[i-1]),4)

        hist= [int(x*255) for x in hist]
        for i in range(rows):
            for j in range(cols):
                Vindice = int(img[i,j,c])
                img[i,j,c]= int (hist[Vindice])
    return img

def rectangle(corner):
    corner = corner.reshape((4, 2))
    cornersResize = numpy.zeros((4, 2), dtype=numpy.float32)
    #Con esto sumamos los valores por fila asi obtener los max y min
    add = corner.sum(1)
    cornersResize[0] = corner[numpy.argmin(add)]
    cornersResize[2] = corner[numpy.argmax(add)]
    #con esto restamos los valores por fila asi obtener los max y min
    sth = numpy.diff(corner, axis=1)
    cornersResize[1] = corner[numpy.argmin(sth)]
    cornersResize[3] = corner[numpy.argmax(sth)]
    return cornersResize

def main(filename, points, color = "color"):
    inputImage = cv2.imread(filename)
    #inputImage = cv2.resize(inputImage,(int(600),int(800)))
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.imshow('image',inputImage)
    #cv2.waitKey(0)
    col,fil,c = inputImage.shape
    #inputImage = cv2.resize(inputImage,(fil,col), interpolation = cv2.INTER_CUBIC)
    pts2 = numpy.float32([[0,0],[fil,0],[fil,col],[0,col]])
    M = cv2.getPerspectiveTransform(points,pts2)
    salida = cv2.warpPerspective(inputImage,M,(fil,col))
    strr = "uploads/solution_"+str(random.random())+".jpg"
    #salida = Histo_Color(salida)
    if(color == "blanco" or color == "grises"):
        salida = cv2.cvtColor(salida, cv2.COLOR_BGR2GRAY)
        if(color == "blanco"):
            salida = cv2.threshold(salida, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite(strr,salida)
    return strr

filename = sys.argv[1]

color = str(sys.argv[10])
#print(color)
inputImage = cv2.imread(filename)
col,fil,c = inputImage.shape
#print(inputImage.shape)
points = numpy.array([[int(sys.argv[2]),int(sys.argv[3])],[int(sys.argv[4]),int(sys.argv[5])],[int(sys.argv[6]),int(sys.argv[7])],[int(sys.argv[8]),int(sys.argv[9])]], numpy.int32)
new_fil = fil/600
new_col = col/800

#print(points)
points = points*[new_fil,new_col]
#print(points)

points = rectangle(points)
#print(points)
print(main(filename,points, color))

