import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from selenium import webdriver
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("I am your Assistant")
            talk("Alexa")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command =   take_command()

    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'about' in command:
        topic = command.replace('about', '')
        topic=topic.replace(' ','+')
        browser =webdriver.Chrome('chromedriver')
        for i in range(1):
            ele=browser.get("https://www.google.com/search?q="+topic+"&start"+str(i))           
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        ab= talk(pyjokes.get_joke())
        print(ab)     
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
