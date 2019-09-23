import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(6)
    camera.capture_sequence([
        'image%02d.jpg' % i
        for i in range(100)
        ])
    camera.stop_preview()
