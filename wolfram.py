import apikeys
import wolframalpha

client = wolframalpha.Client(apikeys.WOLFRAM_KEY);

def getResponse(query):
	res = client.query(query);
	return next(res.results).text;