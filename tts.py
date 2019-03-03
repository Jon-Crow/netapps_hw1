from watson_developer_cloud import TextToSpeechV1
import ClientKeys
import os

#https://watson-developer-cloud-python-sdk.readthedocs.io/en/latest/


text_to_speech = TextToSpeechV1(
    iam_apikey=ClientKeys.IBM_API_KEY,
    url=ClientKeys.IBM_URL
);

def playVoice(speak):
	file = open('voice.wav', 'wb');
	if(isinstance(speak, bytes)):
		speak = speak.decode("utf-8");
	file.write(text_to_speech.synthesize(speak,'audio/wav','en-US_AllisonVoice').get_result().content);
	file.close();
	
