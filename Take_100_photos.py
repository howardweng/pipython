## Camera ##
import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
  count = 1
  for i in range(1, 101):
    camera.resolution = (1024, 768)
    #camera.framerate = 24
    time.sleep(2)
    image_output = np.empty((768, 1024, 3), dtype=np.uint8)
    camera.capture(image_output, 'bgr')
    image_output = np.fliplr(image_output)
    image_output - np.flipud(image_output)
    cv2.imwrite("./detect_img/raspi_cut_" + str(count) + ".jpg" , image_output)
    
    count += 1
    if(i != 100):
      time.sleep(10)
    #cv2.imshow('My Image',image_output)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
