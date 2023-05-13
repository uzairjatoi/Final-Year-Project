from Body.speak import speak 
import datetime
import os
import webbrowser
import smtplib
import wikipedia
import pywhatkit

def Openexe(query):

 while True:

    if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            return  True

    elif 'on youtube' in query:
             pywhatkit.playonyt(query)
             return True

    elif 'google' in query:
             query = query.replace("google", "")
             pywhatkit.search(query)
             return True

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            return True

    elif 'open google' in query:
            webbrowser.open("google.com")
            return True
