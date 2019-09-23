import picamera

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_recording('test_video.h264')
camera.wait_recording(30)
camera.stop_recording()
