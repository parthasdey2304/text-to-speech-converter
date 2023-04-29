#!/bin/python3

# this is a python code that takes a text file as input and converts it to speech
# using the google text to speech api
import os
from gtts import gTTS

# read the text file
filename = input("Enter the filename with extension(should be inside the same folder) : ")
file = open(filename, "r")
text = file.read().replace("\n", " ")

# convert the text to speech
audio = input("Enter the name with which you want to save the audio file(without extension) : " )
tts = gTTS(text=text, lang="en")
tts.save(f"{audio}.mp3")

# closing the file
file.close()

# this is to play the audio file using cvlc
os.system(f"vlc {audio}.mp3")
           
