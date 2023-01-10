import speech_recognition as li
import pywhatkit
import pyttsx3
import datetime
import os
import time
import wolframalpha


converter = pyttsx3.init()

voices = converter.getProperty('voices')
  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)



listner = li.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[4].id)
engine.setProperty('rate', 150)



def talk(text):
    engine.say(text)
    engine.runAndWait()

#funtion for wish you 
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello sir,Good Morning")
        print("Hello sir,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello sir,Good Afternoon")
        print("Hello sir,Good Afternoon")
    else:
        talk("Hello sir,Good Evening")
        print("Hello sir,Good Evening")

#function for opening application
def open_app():
    if 'davinci resolve' in command:
            davinci = "C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe"
            talk("opening davinci......")
            print("opening danvi")
            os.startfile(davinci)
    elif 'notion' in command:
            Notion = "C:\\Users\\User\\AppData\\Local\\Programs\\Notion\\Notion.exe"
            talk("opening notion......")
            print("opening notion")
            os.startfile(Notion)
    elif 'vs code''i need to code' in command:
            Notion = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            talk("you are ready to code sir......")
            print("opening Vs code")
            os.startfile(Notion)



def take_command():
    try:
        with li.Microphone() as source:
            print("listening.....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'light' in command:
                command = command.replace('light','')
                print (command)
            
            

    except :
        pass
        return "None"
    return command


#below all is calling the each function and activate the programe


talk("Loading   your   AI   personal   assistant   light")
wishMe()
while True:
        
        
        command = take_command().lower()
        if command==0:
            continue

        if "goodbye" in command or "ok bye" in command or "stop" in command:
            talk('Good bye sir,see you again')
            print('Good bye sir,see you again')
            break    
        
        if 'good morning' in command:
            plan = command.replace('good morning', '')
            talk('sir what is the plan today, How can i help you?')
        if 'good evening' in command:
            plan = command.replace('good evening', '')
            talk('what about your todays day sir, what the work to done sir?')
                
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'search' in command:
            search = command.replace('please search','')
            talk('give  a  second  sir')
            pywhatkit.search(search)
            talk(search)
            print ("searching.....")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('current time is ' + time)
        elif 'ask' in command:
            talk('I can answer to computational and geographical questions  and what question do you want to ask now')
            question= take_command()
            app_id="LAUL5Y-VTYGTGG5Y5"
            client = wolframalpha.Client('LAUL5Y-VTYGTGG5Y5')
            res = client.query(question)
            answer = next(res.results).text
            talk(answer)
            print(answer)

        elif 'open' in command:
            talk('give a second sir')
            open_app()

        
            

