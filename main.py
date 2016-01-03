import cv2
import os, sys
from datetime import datetime 
from time import strftime
# Camera 0 is the integrated web cam
camera_port = 0
 
ramp_frames = 30

PHOTOS_DIR = ".captures"

homedir = os.path.expanduser("~")
targetDir = os.path.join(homedir, PHOTOS_DIR)
fileName = os.path.join(targetDir, datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".png")


if not os.path.exists(targetDir):
    os.makedirs(targetDir)
 
camera = cv2.VideoCapture(camera_port)
 
def get_image():
	retval, im = camera.read()
	return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
	temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
cv2.imwrite(fileName, camera_capture)
 
del(camera)
