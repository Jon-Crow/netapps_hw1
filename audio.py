import vlc
import subprocess

def play():
	subprocess.Popen(["/usr/bin/cvlc", "/home/pi/Desktop/netapps_hw1/voice.wav"])
