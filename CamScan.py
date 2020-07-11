import cv2
import numpy
import math
import random
import sys

def rectangle(corner):
    corner = corner.reshape((4, 2))
    cornersResize = numpy.zeros((4, 2), dtype=numpy.float32)
    add = corner.sum(1)
    cornersResize[0] = corner[numpy.argmin(add)]
    cornersResize[2] = corner[numpy.argmax(add)]
    sth = numpy.diff(corner, axis=1)
    cornersResize[1] = corner[numpy.argmin(sth)]
    cornersResize[3] = corner[numpy.argmax(sth)]
    return cornersResize

def main(filename, points):
    inputImage = cv2.imread(filename)
    col,fil,c = inputImage.shape
    print(inputImage.shape)
    new_fil = fil/600
    new_col = col/800
    print(points)
    points = points*[new_fil,new_col]
    print(int(points))
    #inputImage = cv2.resize(inputImage,(fil,col), interpolation = cv2.INTER_CUBIC)#cv2.resize(inputImage,(int(600),int(800)))
    pts2 = numpy.float32([[0,0],[fil,0],[fil,col],[0,col]])
    M = cv2.getPerspectiveTransform(points,pts2)
    salida = cv2.warpPerspective(inputImage,M,(fil,col))
    strr = "uploads/solution_"+str(random.random())+".jpg"
    cv2.imwrite(strr,salida)
    return strr

filename = sys.argv[1]

points = numpy.array([[int(sys.argv[2]),int(sys.argv[3])],[int(sys.argv[4]),int(sys.argv[5])],[int(sys.argv[6]),int(sys.argv[7])],[int(sys.argv[8]),int(sys.argv[9])]], numpy.int32)

points = rectangle(points)
#print(points)
print(main(filename,points))

