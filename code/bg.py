import numpy as np
import cv2
cap = cv2.VideoCapture("/home/mart0124/latex/proposal/GOPR7123.MP4")
fgbg = cv2.createBackgroundSubtractorMOG2()
scale=0.4
while(1):
    ret, inf = cap.read()
    if ret:
	frame = cv2.resize(inf, (0,0), fx=scale, fy=scale)
        fgmask = fgbg.apply(frame,frame,0)
        fgmask = cv2.dilate(fgmask, None, iterations=1)
        cv2.imshow('frame',fgmask)
        # Set up the SimpleBlobdetector with default parameters.
        params = cv2.SimpleBlobDetector_Params()
     
        # Change thresholds
        params.minThreshold = 0;
        params.maxThreshold = 256;
     
        # Filter by Area.
        params.filterByArea = True
        params.minArea = 30
     
        # Filter by Circularity
        #params.filterByCircularity = True
        #params.minCircularity = 0.1
     
        # Filter by Convexity
        #params.filterByConvexity = True
        #params.minConvexity = 0.5
     
        # Filter by Inertia
        #params.filterByInertia =True
        #params.minInertiaRatio = 0.5
     
        detector = cv2.SimpleBlobDetector_create(params)
 
        # Detect blobs.
        reversemask=255-fgmask
        keypoints = detector.detect(reversemask)
        im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        cv2.imshow("Keypoints", im_with_keypoints)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
