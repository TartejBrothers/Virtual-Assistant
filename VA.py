import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from pydub import AudioSegment
from pydub.playback import play

r=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
mic = sr.Microphone()
r.energy_threshold=1900

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with mic as source:
            print("Give Input:",end=" ")
            r.adjust_for_ambient_noise(source)
            voice=r.listen(source)
            command= r.recognize_google(voice,language='en-US',key=None)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace("alexa","")
                print(command)
    except:
        command="NO COMMAND GIVEN"
    return command
def run_alexa():
    song = AudioSegment.from_wav("Siri Open.wav")
    play(song)
    command=take_command()
    if "play" in command:
        song=command.replace("play","")
        print("Playing"+song)
        talk("playing"+song)

        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print("Current time is "+ time)
        talk("current time is"+time)
        
    elif "joke" in command:
        a=pyjokes.get_joke()
        print(a)
        talk(a)
while True:   
    run_alexa()
    print()