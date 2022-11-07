import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# it takes command from user and return string


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again sir please...")
        return "None"
    return query

def WishMe():
    ''' It Wishes user'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!")

    elif hour >= 16 and hour < 20:
        speak("Good Evening sir!")

    else:
        speak("Good Night sir!")

    speak("I am Jarvis Ready for your Work sir, Please Tell me how i can help you.")


if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()
        #Logic for executing tasks based on user query
        if 'wikipedia' in query:
            speak('Searching Wikipedia Sir...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'G:\\songs\\my music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'stop' in query:
            quit()

        elif 'code' in query:
            codepath = "C:\\Users\\SAYAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'search' in query:
            try:
                kt.search(query)
            
                speak("According to the google")
                # query = query.replace("google","")
                # results = query.summary(query, sentences=5)
            except:
                speak("Not found sir")

        

        

            

        


