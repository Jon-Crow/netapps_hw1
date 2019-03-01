import vlc

def play():
	player = vlc.MediaPlayer('voice.wav');
	player.play()
	while player.is_playing():
		continue;
	player.stop();
	
play();