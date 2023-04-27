# this is a python code that takes a text file as input and converts it to speech
# using the google text to speech api
from gtts import gTTS
import os

# this is to install the vlc only for linux with apt
os.system("sudo apt install vlc")

# read the text file
file = open("LICENSE", "r")
text = file.read().replace("\n", " ")

# convert the text to speech
tts = gTTS(text=text, lang="en")
tts.save("output.mp3")
file.close()

# this is to play the audio file using cvlc
os.system("cvlc output.mp3")
