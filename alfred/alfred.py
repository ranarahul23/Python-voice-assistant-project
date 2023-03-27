import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def spotify(term):
    
    webbrowser.open("spotify.com")
    speak("this is what i found for your search sir ")
    time.sleep(5)
    pyautogui.moveTo(50, 270)
    pyautogui.click()
    pyautogui.write(term)
    pyautogui.moveTo(840,531)
    time.sleep(4)
    pyautogui.click()

def googleSearch(term):
    result = "https://www.google.com/search?q=" + term
    speak("this is what i found for your search sir")
    webbrowser.open(result)
       
          
def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    speak("this is what i found for your search sir")
    webbrowser.open(result)
    
    pywhatkit.playonyt(term)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        speak("i am alfred sir. please tell me how may i help you")
    elif hour>=12 and hour<18:
        speak("good afternoon")
        speak("i am alfred sir. please tell me how may i help you")
        

    else:
        speak("good evening")
        speak("i am alfred sir. please tell me how may i help you")
       

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio) 
        print(f"User said: {query}\n")  
    except Exception as e:
           
        print("Say that again please...")   
        return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower() 
    
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        elif 'tell me the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strtime}")

        elif "open code" in query:
            codepath="D:\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        elif "open fifa" in query:
            codepath="D:\Games\FIFA 19\FIFA19.exe"
            os.startfile(codepath)
           
            
        elif 'youtube search' in query:
            
            query = query.replace("youtube search","")
            YouTubeSearch(query)
        elif 'open spotify' in query:
            query = query.replace("open spotify","")
            spotify(query)

         
        elif 'thanks mate i will see you later' in query:
            speak("ok sir but i am always here when u need me") 
            break         
        elif 'google search' in query:
            
            query = query.replace("google search","")
            googleSearch(query)
        elif 'open word' in query:
            query = query.replace("open word","")
            codepath="C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(codepath)