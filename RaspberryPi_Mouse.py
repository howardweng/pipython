## Camera ##
import time
import picamera
import numpy as np
import matplotlib.pyplot as plt
import cv2

##  ##

## 1.Get MAC address ##

from uuid import getnode as get_mac
mac = get_mac()
macString = ''.join(("%012x" % mac)[i:i+2] for i in range(0, 12, 2))

#print( macString )


## 2. Start Camera ##

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    #camera.framerate = 24
    time.sleep(2)
    image_output = np.empty((240, 320, 3), dtype=np.uint8)
    start_captime = time.time()
    camera.capture(image_output, 'bgr')
    end_captime = time.time()

#print("start_captime : %s" %start_captime)
#print("end_captime : %s" %end_captime)

#cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

#cv2.imshow('My Image',image_output)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




## Combine Information to json##
import json

data = {
	'Macid': macString,
	'IRstring': 'Empty now',
	'Image_array': image_output.tolist(),
	'Image_timestamp': {'start_captime': start_captime , 'end_captime': end_captime }
}

output = json.dumps(data)

#print(output)


## Mqtt ##
import paho.mqtt.client as mqttClient
 
def on_connect(client, userdata, flags, rc): 
    if rc == 0: 
        print("Connected to broker") 
        global Connected                #Use global variable
        Connected = True                #Signal connection  
    else: 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "68.183.236.150"
port = 1883
user = "frrut"
password = "abc123"
 
client = mqttClient.Client()               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
	time.sleep(0.1)
 
#try:
#    while True:
 
value = output
print(value)

client.publish("python/test",value)


#except KeyboardInterrupt:
 
client.disconnect()
client.loop_stop()
