 # three functions   1. listen  2. translation 3. connect
import speech_recognition as sr
from googletrans import Translator


def listen():
    commond = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening......")
        commond.pause_threshold = 1
        audio = commond.listen(source)

        try:
            print("Recognizing....")
            query = commond.recognize_google(audio,language='en-in')
            print(f"user : {query}\n")
        except  Exception as Error:
            return "none"

        query = str(query).lower()
        return query 

def translation(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"Translation : {data}\n")
    return data 

def MicExecution():
    query = listen()
    data = translation(query)
    return data
   