# import the necessary packages
#from picamera.array import PiRGBArray
#from picamera import PiCamera

import qrtools
#need to install python-qrtools, libzbar-dev. Pillow if needed. 
#in the usr/lib/python2.7/dist-packages Change line 181 from tostring() to tobytes()
 
# initialize the camera and grab a reference to the raw camera capture
#camera = PiCamera()
#rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
#time.sleep(0.1)
 
# grab an image from the camera
#camera.capture(rawCapture, format="bgr")
#image = rawCapture.array
 
# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)
#cv2.waitKey(0)
def decodeQR():
	qr = qrtools.QR()
	qr.decode("qrcode.jpeg")
	return(qr.data)
