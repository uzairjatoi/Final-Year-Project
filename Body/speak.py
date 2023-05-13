import pyttsx3

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voices',voices[1].id)
assistant.setProperty('rate' , 190)

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()
    print(f"Jarvis : {audio}")
    
 
