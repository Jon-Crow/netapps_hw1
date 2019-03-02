#!/usr/bin/env python3

import socket
import cmdargs
import pickle
import crypto
import QR
import tts
import audio
from time import sleep
	
def getQuestion():
	qr = qrtools.QR()
	qr.decode("qrcode.jpeg")
	return(qr.data)
	
def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.connect((serverInfo[0],serverInfo[1]));
	print("\nConnecting to:", serverInfo[0], "on port:", serverInfo[2], "\n");
	print("Listening for QR codes from RPi Camera that contains question \n");
	while 1:
		quest = []
		while not quest:
			QR.captureQR();
			quest = QR.decodeQR();

		quest = quest[0][0];
		if(quest == 'exit'):
			return 0;
		else:
			print("New Question:", quest, "\n");
			
			questenc = pickle.dumps(crypto.encrypt(quest));
			
			print("Sending data:", questenc, "\n");
			
			s.send(questenc);
			
			while 1:
				packet = s.recv(serverInfo[2]);
				if(packet):
					break;
			
			print("Received data:", packet, "\n"); 
			
			decrypted_data = crypto.decrypt(pickle.loads(packet)); 
			
			print("Speaking answer", decrypted_data, "\n");  
			tts.playVoice(decrypted_data);
			audio.play();
			
			sleep(1)
	
		break;
	
	
server = cmdargs.getServerInfo();
if(server == -1 or server[0] == -1):
	print("Invalid arguments");
else:
	start(server);

