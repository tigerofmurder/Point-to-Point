import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys
import random


def Th(img,row,col,x):
	for i in range(row):
		for j in range(col):
			val = img[i,j]
			if val > x:
				img[i,j] = 255
			else:
				img[i,j] = 0

def Not(img,row,col):
	for i in range(row):
		for j in range(col):
			img[i,j] = 255- img[i,j]

def main(img, img1):
	img = cv2.imread(img)
	img2 = cv2.imread(img1)

	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

	row,col = img.shape
	r, c = img2.shape

	Not(img,row,col)
	Not(img2,r,c)
	Th(img,row,col,100)
	Th(img2,r,c,100)

	for i in range (row):
		for j in range(col):
			img[i,j] = img[i,j] | img2[i,j]
	strr = "uploads/solution_"+str(random.random())+".jpg"
	cv2.imwrite(strr,img)
	return strr

filename = sys.argv[1]
filename1 = sys.argv[2]
print(main(filename,filename1))
