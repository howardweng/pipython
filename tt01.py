import picamera
import picamera.array
import cv2
import numpy as np
from time import sleep


left_top = (236,225) 
right_top = (862,85)
left_bot = (96,597)
right_bot = (1000,764)

nleft_top = (236,600)
nright_top = (1024,52)
nleft_bot = (76,959)
nright_bot = (1024,1984)

#background = np.array(1920,1440)

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 32
    #sleep(1)

    with picamera.array.PiRGBArray(camera) as output:
        # camera.capture(output, 'rgb', use_video_port=True)
        count = 500
            
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('./detect_fake/output.avi', fourcc, 20.0, (1024, 768))
        for foo in camera.capture_continuous(output, 'rgb', use_video_port=True):
            print('Captured %dx%d image' % (
            output.array.shape[1], output.array.shape[0]))
            
            
          
            dst = cv2.cvtColor(output.array, cv2.COLOR_RGB2BGR)
         
            dst = np.fliplr(dst)
            dst = np.flipud(dst)
            dst = np.rot90(dst,2) 

            
            dst = cv2.copyMakeBorder(dst,350,900,0,200,cv2.BORDER_CONSTANT,value=[0,0,0])
             
            cv2.line(dst,nleft_top,nright_top,(255,0,0),10)  
             
            cv2.line(dst,nleft_bot,nright_bot,(255,0,0),10)  
            
            #cv2.line(dst,nleft_bot,nright_bot,(255,0,0),10)  
            #cv2.line(dst,nright_bot,nright_top,(255,0,0),10)  
            
            #pts1 = np.float32([[236,575],[1024,52],[76,959],[1024,1984]])
            pts1 = np.float32([list(nleft_top),list(nright_top),list(nleft_bot),list(nright_bot)])

            pts2 = np.float32([[0,0],[1024,0],[0,768],[1024,768]])
            
            M = cv2.getPerspectiveTransform(pts1,pts2)
            dst =  cv2.warpPerspective(dst,M,(1024,768))
            #cv2.namedWindow("img",1)
            #out.write(dst)
            cv2.imwrite("./detect_fake/raspi_img_" + str(count) + ".jpg" , dst)
            count = count + 1
            sleep(3)

            #cv2.imshow("img", dst)
            if cv2.waitKey(1) & 0xFF == ord('q'):
              break

            output.truncate(0)
    out.release()
    cv2.destroyAllWindows()

