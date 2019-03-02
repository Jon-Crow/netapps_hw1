import vlc
import subprocess

def play():
	subprocess.Popen(["/usr/bin/cvlc", "./voice.wav"])
