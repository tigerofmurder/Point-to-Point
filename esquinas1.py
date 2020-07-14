import cv2
import numpy as np 
import sys

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

def mapp(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2),dtype = np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h,axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew

def Eucli_Dist(x1,y1,x2,y2):
	return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def Gausian_Curve(x,sigma):
	x1 = (2*np.pi)* (sigma**2)
	x2 = np.exp(-(x**2)/(2*sigma**2))
	return (1.0/x1) * x2 

def apply_bilateral_filter(source, filtered_image, x, y, diameter, sigma_i, sigma_s):
    hl = diameter//2
    i_filtered = 0
    Wp = 0
    i = 0
    while i < diameter:
        j = 0
        while j < diameter:
            neighbour_x = int(x - (hl - i))
            neighbour_y = int(y - (hl - j))
            if neighbour_x >= len(source):
                neighbour_x -= len(source)
            if neighbour_y >= len(source[0]):
                neighbour_y -= len(source[0])
            gi = Gausian_Curve(source[neighbour_x][neighbour_y] - source[x][y] ,sigma_i)
            gs = Gausian_Curve(Eucli_Dist(neighbour_x, neighbour_y, x, y), sigma_s)
            w = gi * gs
            i_filtered += source[neighbour_x][neighbour_y] * w
            Wp += w
            j += 1
        i += 1
    i_filtered = i_filtered / Wp
    filtered_image[x][y] = int(round(i_filtered))


def bilateral_filter_own(source, filter_diameter, sigma_i, sigma_s):
    filtered_image = np.zeros(source.shape)

    i = 0
    while i < len(source):
        j = 0
        while j < len(source[0]):
            apply_bilateral_filter(source, filtered_image, i, j, filter_diameter, sigma_i, sigma_s)
            j += 1
        i += 1
    return filtered_image


def gaussian_blur(size,sigma):
	kernel = np.zeros((size,size),np.float32)
	m=size//2
	for x in range(-m,m+1):
		for y in range(-m,m+1):
			#x1 = sigma*(2*np.pi)**2
			x1 = (2*np.pi)*(sigma**2)
			x2 = np.exp(-(x**2+y**2)/(2*sigma**2) )
			kernel[x+m,y+m] = (1/x1) * x2
	return kernel


def Convolucion(img,mask):
	maxi = np.amax(img)
	rows,cols= img.shape
	m,n = mask.shape
	new= np.zeros( (rows+m-1,cols+n-1) ) 
	n=n//2
	m=m//2
	filtered_img = np.zeros(img.shape)
	new[m:new.shape[0]-m,n:new.shape[1]-n] = img
	for i in range(m,new.shape[0]-m):
		for j in range(n,new.shape[1]-n):
			temp = new[i-m:i+m+1,j-m:j+m+1]
			result = temp*mask
			filtered_img[i-m,j-n] = result.sum()
	maximo = np.amax(filtered_img)
	c = maxi/maximo  
	filtered_img = filtered_img*c

	return filtered_img.astype(np.uint8)

def erosion(original,kernel):
	copia =  original.copy()
	row,col = original.shape
	r,c = kernel.shape
	total = np.sum(kernel)*255 - 200
	height = r//2
	width = c//2
	for y in range (height,row-height):
		for x in range(width,col-width):
			result = mul(original[y-height:y+height+1,x-width:x+width+1],kernel)
			if result > total:
				copia[y,x] = 255 
			else :
				copia[y,x] = 0
	return copia


def dilation(original,kernel):
	copia =  original.copy()
	row,col = original.shape
	r,c = kernel.shape
	total = np.sum(kernel)*255 - 10
	height = r//2
	width = c//2
	for y in range (height,row-height):
		for x in range(width,col-width):
			result = mul(original[y-height:y+height+1,x-width:x+width+1],kernel)
			if result > 250:
				copia[y,x] = 255 
			else :
				copia[y,x] = 0	
	return copia

def mul(m1,m2):
	x = np.multiply(m1,m2)
	return np.sum(x)


def getPoints(filename): 
	image = cv2.imread(filename)
	rows, cols, channel= image.shape
	origin = image.copy()
	image = cv2.resize(image, (600,800)   )
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#cv2.imshow("gray", gray)
	blurred = Convolucion(gray,gaussian_blur(5,1) )
	#cv2.imshow("blurred", blurred)
	edged = cv2.Canny(blurred,100,150)
	kernel = np.ones((5, 5))
	dilated = dilation(edged, kernel)
	dilated = dilation(dilated, kernel)
	img_ths = erosion(dilated, kernel)
	#dilated = cv2.dilate(edged, kernel, iterations=2)
	#img_ths = cv2.erode(dilated, kernel, iterations=1)
	#cv2.imshow("edged",edged)
	#cv2.imshow("closing",img_ths)

	contours,hierarchy = cv2.findContours(img_ths, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours,key= cv2.contourArea,reverse=True)
	# Area del papel con respecto al documento total
	MAX_COUNTOUR_AREA = (img_ths.shape[1]- 10) * (img_ths.shape[0] - 10 )
	maxAreaFound = MAX_COUNTOUR_AREA * 0.25
	pageContour = np.array([[[5,5]], [[5,img_ths.shape[0]-5]],[[img_ths.shape[1]-5, img_ths.shape[0]-5]],[[img_ths.shape[1]-5,5]]])
	for c in contours:
		p = cv2.arcLength(c,True)
		approx = cv2.approxPolyDP(c,0.03*p,True)

		if len(approx) == 4 and  cv2.isContourConvex(approx) :
			if  maxAreaFound < cv2.contourArea(approx) and cv2.contourArea(approx) < MAX_COUNTOUR_AREA :
				maxAreaFound = cv2.contourArea(approx)
				pageContour = approx
				break
				
	return approx


filename = sys.argv[1]
points = getPoints(filename)

x,y,z = points.shape

arr = [[0,0],[0,0],[0,0],[0,0]]#numpy.zeros(shape=(x,z))

for i in range (0,x):
    for k in range (0,z):
        arr[i][k] =  points[i][0][k]
        
print(arr)
