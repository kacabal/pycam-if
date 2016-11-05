#from SimpleCV import Image, Camera
#cam = Camera()
#img = cam.getImage()
#img.save('tmp.jpg')

from cv2 import *
import time

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
namedWindow("cam-test",CV_WINDOW_AUTOSIZE)

while True:
    s, img = cam.read()
    if s:    # frame captured without any errors
        imshow("cam-test",img)
        if (waitKey(1) != -1):
            break

destroyWindow("cam-test")
