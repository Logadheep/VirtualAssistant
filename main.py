import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(speech):
    engine.say(speech)
    engine.runAndWait()


talk('Welcome Boss! What can I do for you...?')


def take_command():
    original = ''
    command = ''
    try:
        with sr.Microphone() as source:
            print('Waiting for your command')
            voice = listener.listen(source)
            if voice != '':
                try:
                    original = listener.recognize_google(voice)
                    print(original)
                except:
                    talk('It seems you did not speak at this time interval. ')
                    talk('Please make sure you command faster next time')
                    talk("If you spoke before then, it seems the requests has reached the limits...")
                    talk(" Or there must be a problem with your network. I don't receive any words from the google.")
                    sleep(5)
            else:
                talk("It seems the audio is empty... Please try again.")
            command = original.lower()
    except:
        talk('It seems the mic is not working properly... Please check and try again')
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'who are you' in command:
        talk("sir i am your personal voice assistant named helen")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        talk(f'you have been asking me about {person}...! Here is the information I have collected for you')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        topic = command.replace('what is', '')
        talk(f'you have been asking me about {topic}...! Here is the information I have collected for you')
        info = wikipedia.summary(topic, 3)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'google' in command:    
        talk("opening microsoft edge so that you can search on google. ")
        talk("I can't search google myself because I am not that advanced as Siri or Google Assistant or Alexa")
        webbrowser.open('https://google.com')
    elif 'youtube' in command:
        talk("opening Youtube. I can not play any video myself.")
        webbrowser.open('https://youtube.com')
    elif 'music' in command:
        talk("opening Youtube. I can not play any video myself.")
        webbrowser.open_new('https://music.youtube.com')
    elif 'shutdown' in command:
        talk('You are given 20 seconds to save and close all your windows.')
        talk(' Else any data that is not saved may be erased')
        os.system('shutdown /s /t 20')
    elif 'restart' in command:
        talk('The computer might restart sooner... ')
        talk('Please check if there are any updates ready to be installed. ')
        talk('If you need to cancel any updates you can cancel now by saying yes. ')
        talk('If you are sure to restart you may proceed by telling no.')
        value = ('yes' in take_command())
        if value:
            talk('Get ready for the restart.. Please do not plug out your computer till then.')
            os.system('shutdown /r /t 20')
        else:
            talk('The operation was cancelled by user.')
    elif ' end ' in command or ' stop ' in command:
        talk('Are you sure to close me...? Do you want to kill me then? Respond with a yes or no')
        value = ('yes' in take_command())
        if value:
            talk('Thank you for using me...! You can just start me again when you wish by opening the file.')
            talk(' I will try my best next time')
            exit()
        else:
            talk('The operation was cancelled by user.')
            talk('Thanking you for saving me from a gigantic monster kill.')
    else:
        talk('Please say the command again.')

while True:
    run_jarvis()




# jarvis\Scripts\activate.bat
# python main.py