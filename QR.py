import cv2
from pyzbar.pyzbar import decode

#CV2 - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
#QR - https://pypi.org/project/pyzbar/


def captureQR():
	cam = cv2.VideoCapture(0)
	ret, image = cam.read()

	if ret:
		cv2.imshow('Snapshot', image)
		cv2.waitKey(0)
		cv2.destroyWindow('Snapshot')
		cv2.imwrite('./qrcode.jpg', image)

	cam.release()

def decodeQR():
	image = cv2.imread("qrcode.jpg")
	mask = cv2.inRange(image, (0,0,0),(200,200,200))
	thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
	inverted = 255-thresholded
	barcode = decode(inverted)

	return(barcode)

