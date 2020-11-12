import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#importing voice modules

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speaking function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    speak('Welcome aboard! I am real life Jarvis and artificial intelligence assistant')
    speak('Can I help you in anyway?')

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


# wishes the user according to time of the day

def WishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning Noah! Have a Great Day')
    elif hour >= 12 and hour < 17:
        speak('Good Afternoon Noah! How about a nap?')
    elif hour >= 17 and hour < 22:
        speak('Good Evening Noah! How was your day?')
    else:
        speak('Good Night Noah! Sweet Dreams')


# taking audio input from the user and returning it as a string

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('All Ears.....')
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print('Recognizing......')
        query = r.recognize_google(audio)
        print(f'You are saying: {query}\n')

    except Exception as e:
        print('Pardon Please...')
        return 'None'

    return query

# sends email to the entered email
# enter your email and password in login and sendmail

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    welcome()
    while True:
        query = TakeCommand().lower()

    # logics for executing different given tasks

        if 'wikipedia' in query:
            speak('Searching through Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open spotify' in query:
            webbrowser.open('spotify.com')

        elif 'open netflix' in query:
            webbrowser.open('netflix.com')

        elif 'play songs' in query:
            music_dir = 'D:music\\fav'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')

        elif 'the date' in query:
            date()

        elif 'open chrome' in query:
            chrPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrPath)

        elif 'open pycharm' in query:
            pycPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            os.startfile(pycPath)

        elif 'send email' in query:
            try:
                speak('What should i say in the mail')
                content = TakeCommand()
                to = 'youremail@gmail.com'
                sendEmail(to, content)
                speak('Email has been successfully sent')

            except Exception as e:
                print(e)
                speak("Email could not be sent")

        elif 'my name' in query:
            speak('Your name is Noah The God')

        elif 'wish me' in query:
            WishMe()

        elif 'exit' or 'thank you' or 'quit' in query:
            exit()















