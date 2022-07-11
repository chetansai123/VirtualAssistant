from datetime import datetime
from random import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import random
# creating an object and passing the speech API as parameter in it.
engine=pyttsx3.init('sapi5')
# This function will echo the audio which was sent to it... a vitual assist
def echo(sound):
    engine.say(sound)
    engine.runAndWait()
# Getting the rate of voice(speed)    
rate=engine.getProperty('rate')
#Setting the rate to another value 
engine.setProperty('rate',190)# By default it is 200
# Getting the voices 
voices=engine.getProperty('voices')
# Setting the voice
engine.setProperty('voice',voices[0].id)
# Getting the volume of voice
volume=engine.getProperty('volume')
# By default it was also set to 1 
engine.setProperty('volume',1.0)# by default it was 1.0
# This function will take the voice input from user and returns it as query
def UserInput():
    r=sr.Recognizer()#Creating the object for speech recognizer class
    with sr.Microphone() as source:
        audio=r.listen(source)
        r.phrase_threshold=1#This will limit the max time delay between user voice inputs
        print("istening...")
        try:
            print("Recognising...")
# recognize_google() will access the Google web speech API and turn spoken language into text. 
            query=r.recognize_google(audio,language="en-in")
            print(query)
        except Exception as e:
            print("Failed to recognise... Please try again...")
            echo("Failed to recognise... Please try again...")
            return "None"
        return query
# Like the bootengine on computer this fn will be called first whenever it is executed first
def booting():
    hour=int(datetime.now().hour)
    if(hour>0 and hour<12):
        echo("Good Morning sir")
    elif(hour>12 and hour<18):
        echo("Good Afternoon sir")
    else:
        echo("Good Evening sir")
    echo("I am your Virtual Assistant how may i help you?")
if __name__ == '__main__':
    while True:
        query=UserInput().lower()
        if 'wikipedia' in query:
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=1)
            echo("According to Wikipedia")
            print(results)
            echo(results)
        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
        elif 'open youtube' in query:
            webbrowser.open_new("https://www.youtube.com")
        elif 'the time' in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            echo(f"The time is {strTime}")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("https://music.youtube.com/watch?v=ZY5rK7R_nmk&list=MLCT")
        elif 'quit' or 'exit' in query:
            exit()