import sys

def getArg(id):
	for i in range(len(sys.argv)):
		if(sys.argv[i] == id):
			return sys.argv[i+1];
	return -1;
	
def getServerInfo():
	ip = getArg("-sip");
	port = int(getArg("-sp"));
	size = int(getArg("-z"));
	if(port == -1 or size == -1):
		return -1;
	return (ip, port, size);