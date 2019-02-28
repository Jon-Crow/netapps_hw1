import socket
import cmdargs
import pickle
import crypto
import wolfram
import tts

def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print("Created socket at:",serverInfo[0], "on port:", serverInfo[1]);
	s.bind(("",serverInfo[1]));
	s.listen(1);
	print("Listening for client connections");
	client, address = s.accept();
	print("Accepted client connection from:", serverInfo[0], "on port:", serverInfo[1] );
	while 1:
		print("Waiting on question");
		packet = client.recv(serverInfo[2]);
		print("Received data: ", packet);
		if(packet):
			query = crypto.decrypt(pickle.loads(packet));
			
			print("Speaking question:",query);
			tts.playVoice(query);
			
			print("Sending question to Wolfram Alpha:", query );
			ans = wolfram.getResponse(query);
			
			print("Received answer from Wolfram Alpha:", ans);
			
			client.send(pickle.dumps(crypto.encrypt(ans))); 
			
			print("Sending answer:" ,ans); 
		
			
			break; # I got tired of this infinite loop

server = cmdargs.getServerInfo();
if(server == -1):
	print("Invalid arguments");
else:
	start(server);
