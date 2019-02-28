#!/usr/bin/env python3

import socket
import cmdargs
import pickle
import crypto
import qrtools
	
def getQuestion():
	qr = qrtools.QR()
	qr.decode("qrcode.jpeg")
	return(qr.data)
	
def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.connect((serverInfo[0],serverInfo[1]));
	print("Connecting to:", serverInfo[0], "on port:", serverInfo[2]);
	print("Listening for QR codes from RPi Camera that contains question");
	while 1:
		quest = getQuestion();
		if(quest == 'exit'):
			return 0;
		else:
			print("Sending data:", quest);
			s.send(pickle.dumps(crypto.encrypt(quest)));
			
			while 1:
				packet = s.recv(serverInfo[2]);
				if(packet):
					break;
			
			
			print("Received data:", packet); #Undecrypted payload received
			
			decrypted_data = crypto.decrypt(pickle.loads(packet)); # decrypt the payload
			
			print("Speaking answer", decrypted_data);   #speaking the answer
			tts.playVoice(decrypted_data);
	
		break;
	
	
server = cmdargs.getServerInfo();
if(server == -1 or server[0] == -1):
	print("Invalid arguments");
else:
	start(server);

