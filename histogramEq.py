import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys


def sn(L,n,Pn):
	L = L-1
	Pr = 0
	for i in range(0,n,1):
		Pr += Pn[i]
	return L*Pr

def Pn(L,size,pn):
	for x in L:
		pn.append(x/size)


def main(S_n,filename,img):
	height, width = img.shape
	for y in range(0,width):
		for x in range(0,height):
			img[x,y] = S_n[img[x,y]]
	strr = "uploads/"+filename+".jpg"
	cv2.imwrite(strr,img)
	plt.hist(img.ravel(),256,[0,256])
	return strr;


filename = sys.argv[1]
c = float(sys.argv[2])
d = float(sys.argv[3])

imgen = cv2.imread(filename)
img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
L = plt.hist(img.ravel(),256,[0,256])[0]
plt.savefig('uploads/histograma.png')
height, width = img.shape
size = height * width
pn = []
Pn(L,size,pn)
S_n = []
for i in range (1,len(L)+1):
	S_n.append(int(sn(len(L),i,pn)))

print(main(S_n,str(size),img))



