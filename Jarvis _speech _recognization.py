import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
from time import ctime
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

r = sr.Recognizer()



def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)  # Listen for the user's input
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, My speech voice is down')
        return voice_data
    
def respond(voice_data):
    if 'What is your name' in voice_data:
        print('My name is jarvis')
    if 'What time is' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q' + search
        url = 'https://youtube.com/search?'  +search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'open youtube' in voice_data:
        webbrowser.get().open('https://www.youtube.com/')
        print('Here is the youtube')
        while True:
            voice_data = record_audio()
            respond(voice_data)
            if 'exit' in voice_data:
                break
    
time.sleep(1)   #Give a small
print('How can I help You?')
while 1:
    voice_data = record_audio()
    respond(voice_data)