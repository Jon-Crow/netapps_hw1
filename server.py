import socket
import cmdargs
import pickle
import crypto
import wolfram
import tts
import audio
from time import sleep

def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print("\nCreated socket at:",serverInfo[0], "on port:", serverInfo[1], "\n");
	s.bind(("",serverInfo[1]));
	s.listen(1);
	print("Listening for client connections \n");
	client, address = s.accept();
	print("Accepted client connection from:", serverInfo[0], "on port:", serverInfo[1], "\n");
	while 1:
		print("Waiting on question \n");
		packet = client.recv(serverInfo[2]);
		print("Received data: ", packet, "\n");
		if(packet):
			query = crypto.decrypt(pickle.loads(packet));
			
			print("Speaking question:",query, "\n");
			tts.playVoice(query);
			audio.play()
			
			sleep(1)
			
			print("\nSending question to Wolfram Alpha:", query, "\n");
			ans = wolfram.getResponse(query);
			
			print("Received answer from Wolfram Alpha:", ans, "\n");
			
			ansenc = ans.encode('utf-8');
			
			client.send(pickle.dumps(crypto.encrypt(ansenc))); 
			
			print("Sending answer:" ,ans); 
			

server = cmdargs.getServerInfo();
if(server == -1):
	print("Invalid arguments");
else:
	start(server);
