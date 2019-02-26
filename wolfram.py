import apikeys
import wolframalpha

client = wolframalpha.Client(apikeys.WOLFRAM_KEY);

def getResponse(query):
	print("Getting response from wolfram");
	res = client.query(query);
	print("received response");
	return next(res.results).text;