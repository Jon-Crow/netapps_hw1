import vlc

def playVoice():
	player = vlc.MediaPlayer("voice.wav");
	player.play();
	while player.is_playing():
		continue;
	player.stop();
		
playVoice();