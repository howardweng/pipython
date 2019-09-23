import time
import picamera
import numpy as np
import matplotlib.pyplot as plt
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    #camera.framerate = 24
    time.sleep(2)
    output = np.empty((768, 1024, 3), dtype=np.uint8)
    camera.capture(output, 'bgr')

#plt.imshow(output)
#plt.show()

#cv2.cvtColor(output, cv2.COLOR_RBG2BGR)
cv2.imshow('test',output)

cv2.waitKey(0)
cv2.destroyAllWindows()

#print(output)
#print(typeof(output))
