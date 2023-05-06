#!/bin/python3

# importing all the required packages
import os
from gtts import gTTS  # gtts package is used for text-to-speech conversion
from tkinter import *
from tkinter import filedialog
import pygame  # pygame is used to play the generated audio

# creating the root window
root = Tk()
root.geometry("300x200")
root.title("Text to speech converter")
root.config(bg="grey")

# setting the default foreground color to white
fg_color = "white"

# initializing the filepath and audio variables
filepath = ""
audio = "temp_audio_generated.mp3"

# this method is used to open a file dialog and get the selected file's path
def fileOpener():
    global filepath  # using global variable filepath
    filepath = filedialog.askopenfilename()  # opening the file dialog window
    file = open(filepath, "r")  # opening the selected file in read mode
    text = file.read().replace("\n", "   ")  # replacing newline characters with spaces
    text_to_speech_converter(text)  # converting the file's text to speech

# this method is used to get the input text from the Entry widget and convert it to speech
def entrysound():
    text = entry.get()  # getting the input text from the Entry widget
    text_to_speech_converter(text)  # converting the text to speech

# this method is used to convert the given text to speech using the gtts package
def text_to_speech_converter(txt):
    tts = gTTS(text=txt, lang="en")  # creating a gTTS object with English language and input text
    tts.save(audio)  # saving the generated audio as a temporary file
    soundplayer()  # playing the generated audio

# this method is used to play the generated audio using pygame
def soundplayer():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode((1, 1))
    pygame.mixer.music.load(audio)  # loading the generated audio
    pygame.mixer.music.play()  # playing the audio
    while pygame.mixer.music.get_busy():  # waiting for the audio to finish playing
        root.update()  # updating the root window
    pygame.mixer.quit()  # quitting the pygame mixer
    os.system(f"rm {audio}")  # deleting the temporary audio file

# creating the UI elements using tkinter
Label(root, text="Enter the text : ", bg="grey", fg=fg_color).pack()
entry = Entry(root, bg="grey", fg=fg_color)
entry.pack()

Button(root, text="Submit", bg="grey", pady=5, fg=fg_color, command=entrysound).pack(pady=10)

Label(root, text="\nOR\n\nText file : ", bg="grey", fg=fg_color).pack()

Button(root, text="Choose file", command=fileOpener, bg="grey", fg=fg_color).pack()

# setting the foreground color of the root window and running the main event loop
root.mainloop()
