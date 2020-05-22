import cv2
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import sys

def ContrastStretching(filename):
    img = cv2.imread(filename)
    output = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    row,cols = output.shape
    numTotal= row*cols
    bound = int((numTotal * 0.02))
    smallest = np.amin(output)
    biggest = np.amax(output)
    for i in range (row):
        for j in range (cols):
            if (output[i][j] - smallest) < 0:
                output[i][j] = 0
            elif int(output[i][j]- smallest)*(255/int(biggest-smallest)) > 255:
                output[i][j] = 255
            else:
                output[i][j] =  (output[i][j]-smallest)*(255/(biggest-smallest))
    
    strr = "uploads/"+str(numTotal)+".jpg"
    cv2.imwrite(strr,output)
    return strr
    
filename = sys.argv[1]
c = float(sys.argv[2])
d = float(sys.argv[3])

print(ContrastStretching(filename))
