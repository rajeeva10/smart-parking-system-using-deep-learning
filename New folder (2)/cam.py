import cv2
import time
import sys
import os

##             to open cam and show the frame
##cam = cv2.VideoCapture(0)
##while True:
##    _, image_frame=cam.read()
##    cv2.imshow('frame',image_frame)
##    cv2.waitKey(1)
##cam.release()

##

cam = cv2.VideoCapture(0)
while True:
    _, image_frame=cam.read()
    cv2.imshow('frame',image_frame)
    cv2.imwrite('photo.png',image_frame)
    time.sleep(2)
cam.releas()
