import cv2
import numpy as np 
import math
import sys

def logarithm(c,f):
	value = int(c*math.log(1+f,10))
	if(value>255):
		return 255
	elif(value<0):
		return 0
	return value

def main(cons,img):
	height, width = img.shape

	for y in range(0,width):
		for x in range(0,height):
			img[x,y] = logarithm(cons,img[x,y])
	strr = "uploads/"+str(cons)+".jpg"
	cv2.imwrite(strr,img);
	return strr;


filename = sys.argv[1]
c = float(sys.argv[2])
imgen = cv2.imread(filename)
img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
print(main(c,img))

