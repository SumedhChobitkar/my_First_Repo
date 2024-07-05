import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print("say anything ....")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
        if 'alexa' in command:
            command =command.replace('alexa', '')
            print(command) 

    except:
        pass 
    return command

engine.say('hello sumedh ,im your alexa')
engine.say('how can i help you')
engine.runAndWait()
def run_alexa():
    
    command = take_command()
    print(command)
    if 'play' in command:
        song =command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'who is mahatma gandhi ' in command:
        person =command.replace('who is mahatma gandhi ','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif ' are you single ' in command :
        talk(' i am in a relationship with wifi')
    elif ' joke'in command:
        talk(pyjokes.get_joke())
        talk('hahahaha')
    else :
        talk('please say again i didnt understand')

while True:
    run_alexa() 
