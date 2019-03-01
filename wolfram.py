import ServerKeys
import wolframalpha

client = wolframalpha.Client(ServerKeys.WOLFRAM_KEY);

def getResponse(query):
	res = client.query(query);
	return next(res.results).text;
