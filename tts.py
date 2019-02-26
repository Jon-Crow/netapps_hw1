from watson_developer_cloud import TextToSpeechV1
import apikeys
from playsound import playsound
import os

text_to_speech = TextToSpeechV1(
    iam_apikey=apikeys.IBM_API_KEY,
    url=apikeys.IBM_URL
);

def playVoice(speak):
	file = open('voice.wav', 'wb');
	if(isinstance(speak, bytes)):
		speak = speak.decode("utf-8");
	file.write(text_to_speech.synthesize(speak,'audio/wav','en-US_AllisonVoice').get_result().content);
	file.close();
	#playsound(os.path.abspath('voice.wav'));
	