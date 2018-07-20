import cv2
import numpy as np
cap = cv2.VideoCapture("D:\\users\\Home\\Videos\\GOPR7129.MP4")
#cap = cv2.VideoCapture("/home/mart0124/latex/proposal/GOPR7121.MP4")
scale=0.5
i=0

while (1):
	ret, frame = cap.read()
	if ret:
		resized = cv2.resize(frame, (0,0), fx=scale, fy=scale)
		#if i==100:
		#	cv2.imwrite("setup.jpg",resized)
		#if i==950:
		#	cv2.imwrite("action.jpg",resized)
		cv2.imshow("video",resized)
		key = cv2.waitKey(0)& 0xFF
	i+=1
	print(key)
	# if the `q` key was pressed, break from the loop
	if key == ord("p"):
		cv2.imwrite("temp.jpg",resized)
	if key == ord("q"):
		break
