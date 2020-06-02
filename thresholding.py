import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys

def main(value_thr,value_default,img):
    height, width = img.shape
    for y in range(0,width):
        for x in range(0,height):
            if (value_thr <= img[x,y] and img[x,y] <= value_default):
                img[x,y] = 250
            else:
                img[x,y] = 0
    strr = "uploads/"+str(value_thr)+"_"+str(value_default)+".jpg"
    cv2.imwrite(strr,img);
    return strr;


filename = sys.argv[1]
c = float(sys.argv[2])
d = float(sys.argv[3])

imgen = cv2.imread(filename)
img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
plt.hist(img.ravel(),256,[0,256])
plt.savefig('uploads/histograma.png')
print(main(c,d,img))
