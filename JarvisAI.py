import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import openai
import config
from Sites_and_app import sites,apps

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = config.apikey
    chatStr += f"User: {query}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except Exception as e:
        print("Sorry, Some error occurred")
        speak("Sorry, Some error occurred")
    try:
        print(response["choices"][0]["text"])
    except Exception as e:
        quit()
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"


def takeinput():
    with sr.Microphone() as source:
        audio = sr.Recognizer().listen(source)
        try:
            print("Recognizing...")
            query = sr.Recognizer().recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            speak("Sorry, Some error occurred")
            print("Sorry, Some error occurred")
            exit()


if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    speak("Hello, I am Jarvis A.I.")
    while True:
        print("Listening")

        query = takeinput()

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir..")
                try:
                    webbrowser.open(site[1])
                except Exception as e:
                    speak("Sorry, Some error occurred")
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                speak(f"Opening {app[0]} sir..")
                try:
                    os.startfile(app[1])
                except Exception as e:
                    speak("Sorry, Some error occurred")
                    print("Sorry, Some error occurred")
        if 'open music'.lower() in query.lower():
            speak("Starting Music...")
            try:
                os.startfile("C:\\Users\inspi\Music\\01_-_Hamari_Adhuri_Kahani-(MyMp3Singer.com).mp3")
            except Exception as e:
                print("Sorry, Some error occurred")
                speak("Sorry, Some error occurred")
        elif 'the time'.lower() in query.lower():
            speak(datetime.datetime.now().strftime('%H:%M:%S'))
        elif "Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
