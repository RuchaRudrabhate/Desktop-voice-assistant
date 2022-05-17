from pip import main    
import datetime 
import pyttsx3 
import speech_recognition as sr 
import wikipedia
import webbrowser  
import os  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)
def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning !")
    elif hour >=12 and hour<16:
        speak("good afternoon!")
    elif hour >=16 and hour<22:
        speak("Good Evening !")
    else:
        speak("Good Night!!")
    speak("I am Jarvis Master , Please tell me how may I help you!!")
def takecommand():
    #it takes the microphone input from the user and returns string output
    r = sr.Recognizer()#it will recognize the audio
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1       # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said = {query}\n")
    except Exception as e :
        #print(e)
        print("say that again please...")
        return "none"
    return query
    
    
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
    #logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia,")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"master, the is {strtime}")
        elif 'thank you' in query:
            speak("you are welcome..")
        elif 'who are you' in query:
            print("I am your Desktop Assistant. I can help you find answers get things done,and have fun!!")
            speak("I am your Desktop Assistant. I can help you find answers get things done,and have fun!!")
        elif 'open code' in query:
            codepath = "C:\\Users\\arudr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
                
        
            