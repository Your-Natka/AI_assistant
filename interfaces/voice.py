import speech_recognition as sr
import pyttsx3
from core.ai import ask_ai

engine = pyttsx3.init()
r = sr.Recognizer()

def run_voice():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        reply = ask_ai(text)
        engine.say(reply)
        engine.runAndWait()
