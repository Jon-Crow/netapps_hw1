#import qrtools
from pyzbar.pyzbar import decode
from PIL import Image

def decodeQR():
	#qr = qrtools.QR()
	#qr.decode("qrcode.jpeg")
	#return(qr.data)

	value = decode(Image.open("qrcode.jpeg"))
	return(value[0][0])
	
