import socket
import cmdargs
import pickle
import crypto
import wolfram
import tts

def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.bind(("",serverInfo[1]));
	s.listen(1);
	client, address = s.accept();
	while 1:
		packet = client.recv(serverInfo[2]);
		if(packet):
			query = crypto.decrypt(pickle.loads(packet));
			print(query);
			tts.playVoice(query);
			ans = wolfram.getResponse(query);
			print(ans);
			tts.playVoice(ans);

server = cmdargs.getServerInfo();
if(server == -1):
	print("Invalid arguments");
else:
	start(server);