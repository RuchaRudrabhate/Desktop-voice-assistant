from pip import main    #inbuilt
import datetime #inbuilt
import pyttsx3 #pip install pyttsx3  # text to speech
import speech_recognition as sr     # audio to text
import wikipedia    #pip install wikipedia
import webbrowser  #inbuilt                    webbrrowser controller
import os   #inbuilt
import smtplib  #inbuilt
engine = pyttsx3.init('sapi5')  #sapi5 for speech recognition
voices = engine.getProperty('voices')
print(voices) 
engine.setProperty('voice', voices[1].id)
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
    speak("I am Rebecca Master , Please tell me how may I help you!!")
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
        speak("say that again please...")
        return "none"
    return query

def sendEmail(to , content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rudrabhaterucha@gmail.com','abcd1234@')
    server.sendmail('rudrabhaterucha@gmail.com',to,content)
    server.close()

    
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        #searching wikipedia
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            try:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences = 2)
                speak("According to wikipedia,")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry master, I am not able to get required page on wikipedia!!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        #playing music55
        elif 'play music' in query:
            music_dir = "C:\\rucha python files\\JARVIS_\\music"
            songs = os.listdir(music_dir)
            print(songs)
            speak("please tell me song number in 0 to 12")
            n  = int(input("song number  = "))
            print("playing!")
            speak("playing!")
            os.startfile(os.path.join(music_dir,songs[n]))
        #getting time
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"master, the time is {strtime}")
        #opening applications
        elif 'open vs code' in query:
            speak("opening, please wait a second")
            codepath = "C:\\Users\\arudr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open chrome" in query:
            speak("opening, please wait a second")
            a = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(a)
        elif "open pycharm" in query:
            speak("opening, please wait a second")
            wpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(wpath)
        #sending email
        elif 'email to user' in query:
            try:                    #used try except - for not directily teminate prog if error is occured
                speak("what should I say?")
                content = takecommand()
                to = "rudrabhaterucha@gmail.com"
                sendEmail(to,content)
                print("Email is successfully sent!!")
                speak('Email is sent!')
            except Exception as e:
                print(e)
                speak("sorry master i am not able to sent this email!!")
        elif 'thank you' in query:
            speak("you are welcome..")
        elif 'who are you' in query:
            print("I am your Desktop Assistant. I can help you find answers, get things done,and have fun!!")
            speak("I am your Desktop Assistant. I can help you find answers,get things done,and have fun!!")
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "turn off" in query:
            speak("Turning off ! See you again!!")
            exit()
                
        
            