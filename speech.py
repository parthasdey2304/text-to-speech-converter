#!/bin/python3

# importing all the required packages
import os
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
import pygame

# creating the root
root = Tk()
root.geometry("300x400")
root.title("Text to speech converter")
# root.resize(False, False)
root.config(bg = "grey")

filepath = ""
audio = "temp_audio_generated.mp3"

# all the methods are here
def fileOpener():
	filepath = filedialog.askopenfilename()
	file = open(filepath, "r")
	text = file.read().replace("\n", "   ")
	text_to_speech_converter(text)

def entrysound():
	text = entry.get()
	text_to_speech_converter(text)

def text_to_speech_converter(txt):
	tts = gTTS(text = txt, lang = "en")
	tts.save(audio)
	soundplayer()

def soundplayer():
	pygame.init()
	pygame.mixer.init()
	pygame.display.set_mode((1, 1))
	pygame.mixer.music.load(audio)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		root.update()
	pygame.mixer.quit()
	os.system(f"rm {audio}")

Label(root, text="Enter the text : ", bg="grey").pack()
entry = Entry(root, bg="grey")
entry.pack()

Button(root, text="Submit", bg="grey", pady=5, command=entrysound).pack(pady=10)

Label(root, text="\nOR\n\nText file : ", bg="grey").pack()

Button(root, text="Choose file", command=fileOpener, bg="grey").pack()

root.mainloop()
