import cv2
import numpy
import math
import random
import sys

def esquinas(blur):
	edged = cv2.Canny(blur, 35, 45)
	c,h = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	sortedContors = sorted(c, key=cv2.contourArea, reverse=True)
	for i in sortedContors:
		p = cv2.arcLength(i, True)
		points = cv2.approxPolyDP(i, 0.1*p, True)

		if len(points) == 4:
			target = points
			break
	return points

filename = sys.argv[1]
inputImage = cv2.imread(filename)
inputImage = cv2.resize(inputImage,(600,800), interpolation = cv2.INTER_CUBIC)#cv2.resize(inputImage,(int(600),int(800)))
grayInput=cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
blurredInput = cv2.GaussianBlur(grayInput, (1,1), 0)

points = esquinas(blurredInput)

x,y,z = points.shape

arr = [[0,0],[0,0],[0,0],[0,0]]#numpy.zeros(shape=(x,z))

for i in range (0,x):
    for k in range (0,z):
        arr[i][k] =  points[i][0][k]
        
print(arr)
#print([[1,2],[3,4]])
