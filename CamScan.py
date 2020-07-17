import cv2
import numpy
import numpy as np
import math
import random
import sys
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey , imwrite

def threshold_A( img):
	window = 11
	C = 2
	row,col = img.shape[:2]
	img_out = img.copy()
	for i in range(1,row):
		for j in range(1,col):
			y0 = i - int(window/2)
			y1 = i + int(window/2)+1
			x0 = j - int(window/2)
			x1 = j + int(window/2)+1
			if(y0 < 0):
				y0 = 0
			if(y1 > row):
				y1 = row
			if(x0 < 0):
				x0 = 0
			if(x1 > col):
				x1 = col
			block = img[y0:y1,x0:x1]
			thresh = np.mean(block) - C
			if(img[i,j] < thresh):
				img_out[i,j] = 0
			else:
				img_out[i,j] = 255
	return img_out

def complement_conv( img,w, block_size):
    #print("entre")
    row,col = img.shape[:2]
    dst_height = col - block_size[1] + 1
    dst_width = row - block_size[0] + 1
    image_array = np.zeros((dst_height * dst_width, block_size[1] * block_size[0]))
    row_A = 0
    for i in range(w,row-w):
        for j in range(w,col-w):
            y0 = i - int(w)
            y1 = i + int(w)+1
            x0 = j - int(w)
            x1 = j + int(w)+1
    
            if(y0 < 0):
                y0 = 0
            if(y1 > row):
                y1 = row
            if(x0 < 0):
                x0 = 0
            if(x1 > col):
                x1 = col
            block = img[y0:y1,x0:x1]
            image_array[row_A,:] = np.ravel(block)
            row_A+=1
    return image_array


def Convolucion(image, filter_kernel):
    row, col = image.shape[:2]
    i_size , j_size = filter_kernel.shape[:2]
    #print(k_size)
    pad_size = i_size // 2
    #print(pad_size)
    # Pads image with the edge values of array.
    
    image_temp = np.pad(image, pad_size, mode="edge") # funcion pad agrega a los bordes valores repetidos de la imagen
    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = complement_conv(image_temp,pad_size , (i_size, j_size))

    #  turn the kernel into shape(k*k, 1)
    kernel_array = np.ravel(filter_kernel)
    # reshape and get the dst image
    dst = np.dot(image_array, kernel_array).reshape(row, col)
    return dst

def add (imag):
    img = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)
    #img = cv2.medianBlur(img,5)
    sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    #blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
    blur = np.ones((7,7))/49
    #print(blur)
    img = Convolucion(img, blur).astype(np.uint8)
    #img = cv2.filter2D(img,-1,blur)
    #img = Convolucion(img, blur).astype(np.uint8)
    #img = Convolucion(img, blur).astype(np.uint8)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    (fil,col) = th3.shape
    #th3 = threshold_A(img)
    for i in range(fil):
        for j in range(col):
            if(th3[i,j]==0):
                imag[i,j,0] = th3[i,j]
                imag[i,j,1] = th3[i,j]
                imag[i,j,2] = th3[i,j]
    
    return imag

def rectangle(point):
    
    point = point.reshape((4, 2))
    pointsResize = numpy.zeros((4, 2), dtype=numpy.float32)
    #Con esto sumamos los valores por fila asi obtener los max y min
    add = point.sum(1)
    pointsResize[0] = point[numpy.argmin(add)]
    pointsResize[2] = point[numpy.argmax(add)]
    #con esto restamos los valores por fila asi obtener los max y min
    sth = numpy.diff(point, axis=1)
    pointsResize[1] = point[numpy.argmin(sth)]
    pointsResize[3] = point[numpy.argmax(sth)]
    return pointsResize

def GetPerspectiveTransform(pi,ps):
	x1,y1 = pi[0]
	x2,y2 = pi[1]
	x3,y3 = pi[2]
	x4,y4 = pi[3]
	xx1,yy1 = ps[0]
	xx2,yy2 = ps[1]
	xx3,yy3 = ps[2]
	xx4,yy4 = ps[3]
	A = np.array([  [x1,y1,1,0,0,0,  -x1*xx1, -xx1*y1 ],
					[0,0,0,x1,y1,1,  -x1*yy1, -y1*yy1],
					[x2,y2, 1,0,0,0, -x2*xx2, -xx2*y2], 
					[0,0,0,x2,y2,1,  -x2*yy2, -y2*yy2],
					[x3,y3,1,0,0,0,  -x3*xx3, -xx3*y3],
					[0,0,0,x3,y3,1,  -x3*yy3, -y3*yy3],
					[x4,y4,1,0,0,0,  -x4*xx4, -xx4*y4],
					[0,0,0,x4,y4,1,  -x4*yy4, -y4*yy4]
					 ],np.float32)
	#print(A)
	ps = ps.flatten()
	x = cv2.solve(A,ps)
	x = x[1].flatten()
	x = np.append(x,np.float32(1))
	M = x.reshape(3,3)
	return M


def main(inputImage, points, color = "color"):
    #inputImage = cv2.imread(filename)
    #inputImage = cv2.resize(inputImage,(int(600),int(800)))
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.imshow('image',inputImage)
    #cv2.waitKey(0)
    col,fil,c = inputImage.shape
    #inputImage = cv2.resize(inputImage,(fil,col), interpolation = cv2.INTER_CUBIC)
    pts2 = numpy.float32([[0,0],[fil,0],[fil,col],[0,col]])
    #M = cv2.getPerspectiveTransform(points,pts2)
    M = GetPerspectiveTransform(points,pts2)
    salida = cv2.warpPerspective(inputImage,M,(fil,col))
    strr = "uploads/solution_"+str(random.random())+".jpg"
    #salida = Histo_Color(salida)
    #salida = contrast(contrast(salida))
    salida = add(salida)
    #salida = cv2.medianBlur(salida,5)
    if(color == "blanco" or color == "grises"):
        salida = cv2.cvtColor(salida, cv2.COLOR_BGR2GRAY)
        if(color == "blanco"):
            salida = cv2.threshold(salida, 60, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(strr,salida)
    return strr

filename = sys.argv[1]

color = str(sys.argv[10])
#print(color)
inputImage = cv2.imread(filename)
#inputImage = cv2.resize(inputImage,(2400,1800), interpolation = cv2.INTER_CUBIC)
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
print(main(inputImage,points, color))

