import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cv2

# initialize speech recognition
r = sr.Recognizer()

# initialize text-to-speech engine
engine = pyttsx3.init()

# set voice rate and volume
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# define Jarvis's responses
greetings = ["hello", "hi", "hey", "what's up"]
greeting_responses = ["Hello, how can I assist you?", "Hi there, what can I do for you?", "Hey, what's up?", "Howdy! How can I help you today?"]
goodbyes = ["bye", "goodbye", "see you later", "see ya"]
goodbye_responses = ["Goodbye!", "See you later!", "Farewell!", "Have a good one!"]

# define function for Jarvis to respond to user
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define function for Jarvis to perform a web search
def search_web(query):
    url = 'https://www.google.com/search?q=' + query
    webbrowser.get().open(url)
    speak('Here is what I found for ' + query)

# define function for Jarvis to play music from Spotify
def play_music():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_saved_tracks()
    if len(results['items']) == 0:
        speak("Your Spotify library is empty.")
        return
    track = results['items'][0]['track']
    sp.start_playback(uris=[track['uri']])
speak("Now playing " + track['name'] + " by " + track['artists'][0]['name'])



# define function for Jarvis to open YouTube
def open_youtube():
    webbrowser.get().open('https://www.youtube.com/')
    speak('Opening YouTube...')

# define function for Jarvis to draw a rectangle
def draw_rectangle():
    img = cv2.imread('sample_image.jpg')
    cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 3)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# initialize Jarvis
speak("Hello, I'm Jarvis. How can I assist you?")

# start listening for commands
while True:
    # ask user for input method
    speak("Would you like to type or speak your command?")
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        input_method = r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        continue
    except sr.RequestError as e:
        speak("Sorry, there was an error. Please try again later.")
        continue

    # handle input method
    if "type" in input_method:
        speak("Please type your command:")
        command = input()
    elif "speak" in input_method:
        speak("Please say your command:")
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            continue
        except sr.RequestError as e:
            speak("Sorry, there was an error. Please try again later.")
            continue

    # handle command
    if command in greetings:
        response = random.choice(greeting_responses)
        speak(response)
    elif command in goodbyes:
        response = random.choice(goodbye_responses)
        speak(response)
    elif 'search' in command:
        search_term = command.split('search')[1].strip()
        search_web(search_term
