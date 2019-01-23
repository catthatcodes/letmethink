import cv2
import numpy as np
import imutils

def coordinates(img):
	#img = cv2.imread("floor4.jpg")
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
	thresh = cv2.erode(thresh, np.ones((3,3), np.uint8), iterations=2)
	edges = cv2.Canny(thresh, 30, 200)
	contours = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)
	contours = sorted(contours, key = cv2.contourArea, reverse=True)[:3]
	#cv2.drawContours(img, contours, -1, (0,255,0), 2)	
	floor = None
	for c in contours:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.015*peri,True)
		if(len(approx) == 4):
			floor = approx
			break
	#cv2.drawContours(img, floor, -1, (0,0,255), 2)		
	coords = floor.reshape(4,2)
	return coords
"""
cv2.imshow("thresh", thresh)
cv2.imshow("edges", edges)
cv2.imshow("image", img)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
"""