import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand ")
            
            
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    if "Jarvish" in sptext().lower():
        while True:
            datal = sptext().lower()
            if "your name" in datal:
                name = "My name is jarvish"
                speechtx(name)
            elif "old are you" in datal:
                age = "I am two year old"
                speechtx(age)

            elif 'time' in datal:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'youtube' in datal:
                webbrowser.open("https://www.youtube.com/")

            elif 'whatsapp' in datal:
                webbrowser.open("https://www.whatsapp.com/")

            elif 'joke' in datal:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                speechtx(joke_1)
            elif 'play song' in datal:
                add = "D:\song"
                listsong = os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))

            elif 'exit' in datal:
                speechtx("Thank you")
                break

            time.sleep(5)
    
else:
    print("thanks")