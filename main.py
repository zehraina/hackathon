import smtplib
from winreg import QueryInfoKey
import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

t =int(datetime.datetime.now().hour)


def wish(): 
        if t>=12 and t<18 :
            engine.say("Good afternoon")
            engine.runAndWait()
        elif t<12:
            engine.say("Good morning")
            engine.runAndWait()
        else:
            engine.say("good evening")
            engine.runAndWait()       
        engine.say("this is your personal desktop assistant. How may I help you sir? ")
        engine.runAndWait()  



def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio)     
        print("You said:", query)
    except Exception as e:
        print("I didn't quite get you. Could you say that again?")
        engine.say("I didn't quite get you. Could you say that again?")
        engine.runAndWait()
        return "None"
    return query
wish()
query=commands()
while True:
    query=commands().lower()
    if 'wikipedia' in query:
        speak("searching Wikipedia...")
        query=query.replace("wikipedia", "")
        result=wikipedia.summary(query, sentences=2)
        speak("according to Wikipedia...")
        print(result)
        speak(result)
    elif 'open youtube' in query:
        speak("sure")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        speak("sure")
        webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get('chrome').open("google.com", new=2 ) 
    elif 'play music' in query:
        speak("sure")
        music_dir = 'C:\\Users\\inaze\\Documents\\fav'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' or "what is the time" in query:
        speak("sure")
        time=datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is")
        speak(time)
    elif 'open code' in query:
        speak("sure")
        os.startfile("C:\\Users\\inaze\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    
    elif 'open spotify'  in query:
        speak("sure")
        os.startfile("C:\\Users\\inaze\\AppData\\Roaming\\Spotify\\Spotify.exe")

    elif 'search google for'  in query:
        speak("sure")
        search_word=query.replace("search google", "")
        webbrowser.open('http://google.com/search?q=' +search_word)

    elif 'Suggest some trending songs 'in query:
        speak("okay,here we go")
        webbrowser.open("https://www.youtube.com/results?search_query=trending+songs")

    elif 'what is your name' in query:
        speak("hey there nice to meet you . U can call me Elik") 

    elif 'what is the weather of today?'or'what is todays weather?' in query:  
        speak("okay sure")   
        webbrowser.open('http://google.com/search?q=' +"today weather")
        

        
        

    

  
   


  



