from Brain.AIbrain import ReplyBrain
from Body.listen import MicExecution
print ("starting jarvis..... wait some seconds")
from Body.speak import speak 
import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import psutil

def MainExecution():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")  

    while True:
        Data = MicExecution()
        Data = str(Data)

        if ' the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:")    
            speak(f"Sir, the time is {strTime}")

        elif 'wikipedia' in Data:
            speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'on youtube' in Data:
             pywhatkit.playonyt(Data)
             

        elif 'on google' in Data:
             Data = Data.replace("on google", "")
             pywhatkit.search(Data)
             

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")
            

        elif 'open google' in Data:
            webbrowser.open("google.com")
        
        elif 'battey percantage' in Data:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir syestem battery is {percentage} percent")

        elif "bye bye" in Data:
            speak ("thanks sir have a good day!")
            break

        elif "launch" in Data:   
                Data = Data.replace("launch", "")
                pyautogui.press("super")
                pyautogui.typewrite(Data)
                pyautogui.sleep(2)
                pyautogui.press("enter") 

        else:    
        
            Reply = ReplyBrain(Data)
            speak(Reply)

MainExecution()