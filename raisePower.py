import cv2
import numpy as np 
import math
import cmath
import sys

def raise_to(c,r,f):
	value = int(c*(f**r))
	if(value>255):
		return 255
	if(value<0):
		return 0
	return value


def main(cons,cons1,img):
	height, width = img.shape

	for y in range(0,width):
		for x in range(0,height):
			img[x,y] = raise_to(cons,cons1,img[x,y])
	strr = "uploads/"+str(cons)+"_"+str(cons1)+".jpg"
	cv2.imwrite(strr,img);
	return strr;


filename = sys.argv[1]
c = float(sys.argv[2])
r = float(sys.argv[3])

imgen = cv2.imread(filename)
img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
print(main(c,r,img))
