import time
import picamera
import cv2
import numpy
import io

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768 )
    camera.start_preview()
    camera.rotation = 0
    time.sleep(2)
    camera.preview.window=(0,0,1024,768)
    time.sleep(1000)
    camera.stop_preview()
    camera.close()

