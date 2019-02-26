#!/usr/bin/env python3

import socket
import cmdargs
import pickle
import crypto
	
def getQuestion():
	return input("Question:");
	
def start(serverInfo):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.connect((serverInfo[0],serverInfo[1]));
	while 1:
		quest = getQuestion();
		if(quest == 'exit'):
			return 0;
		else:
			s.send(pickle.dumps(crypto.encrypt(quest)));
	
	
server = cmdargs.getServerInfo();
if(server == -1 or server[0] == -1):
	print("Invalid arguments");
else:
	start(server);

