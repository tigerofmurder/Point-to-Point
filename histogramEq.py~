import cv2
import numpy as np
from matplotlib import pyplot as plt

def sn(L,n,Pn):
	L = L-1
	Pr = 0
	for i in range(0,n,1):
		Pr += Pn[i]
	return L*Pr

def Pn(L,size,pn):
	for x in L:
	        pn.append(x/size)

imgc= cv2.imread('hist6.jpg')
img = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)

cv2.imshow('Coverted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.axis("on")
L = plt.hist(img.ravel(),256,[0,256])[0]
print(L)
plt.show()

height, width = img.shape
size = height * width


print(size)

pn = []
Pn(L,size,pn)
S_n = []
for i in range (1,len(L)+1):
	S_n.append(int(sn(len(L),i,pn)))

for y in range(0,width):
	for x in range(0,height):
		img[x,y] = S_n[img[x,y]]
cv2.imshow('Coverted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img.ravel(),256,[0,256])
plt.show()

