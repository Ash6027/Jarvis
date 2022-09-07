import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import sys
import string
import random
import time
from plyer import notification
engine=pyttsx3.init('sapi5')


chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
client =wolframalpha.Client('GRL772-E23GV877ER')

def speak(audio):
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',143)
    engine.say(audio)
    engine.runAndWait()

def speak1(audio):
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak("Morning Buddy")
        speak("Did you sleep well")
           
    elif h>=12 and h<=18:
        speak("Good Afternoon")
        speak("Had lunch buddy")
        speak("how is your day going ")
    else:
        speak("Good Evening buddy")
        speak("how was your day")
        
def cmd():
    r = sr.Recognizer()                                                                                  
    with sr.Microphone(device_index=1) as source:                                                                       
        print("Listening...")
        speak("I am listiening")
        r.energy_threshold =300
        r.dynamic_energy_ratio = 1.5
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('you:' + query + '\n')    
    except Exception :
        print("Say that again......")
        return "None"
    return query


   

def sendEmail(to,content):
    
       server=smtplib.SMTP('smtp.gmail.com',587)
       server.ehlo()
       server.starttls()
       server.login('ashishsharma6027@gmail.com','Ashish@11')
       server.sendmail('ashishsharma6027@gmail.com',to,content)
       server.close()
       
if __name__ == "__main__":
    wish()
    while True:
           query=cmd()
           query=query.lower()
           if 'wikipedia' in query:
               speak('Searching...')
               print("wikipedia....")
               results= wikipedia.summary(query,sentences=2)
               print(results)
               speak(results)
           elif 'Who are you 'in query :
               speak("I Am jarvis")
           

           elif 'it was a good' in query or 'it was a nice day' in query or 'today is a very nice day' in query or 'very good day went ' in query:
                speak("Well done brother")

           elif 'nice work' in query :
               speak1("thanks younger one")

           elif 'bad day'in query or 'worst day'in query or 'very bad day' in query:
                speak("its ok brother")
                speak("Today was just one day")
                file=open("D:/ASHISH/jarvis/quotes")
                g=file.readline()
                speak(g)

           elif 'notify me ' in query or'notify'in query or'remind' in query or'remind me' in query :
                   notification.notify( title="stud", message="study hard", timeout=10)
                   time.sleep(60*60)

        
               
           elif 'open youtube' in query :
               webbrowser.get(chrome).open("youtube.com")
               
           elif 'send mail' in query:
                try:
                   speak("what should i say")
                   content=cmd()
                   to="ashishsharma6027@gmail.com"
                   sendEmail(to,content)
                   speak("Email sent")
                except Exception as e:
                    print(e)
                    speak("Net connection Weak")
                    
           elif 'play music' in query:
                     mus_dir='F:\\music'
                     song=os.listdir(mus_dir)
                     i=random.randrange(0,100)
                     os.startfile(os.path.join(mus_dir, song[i]))
                     speak("enjoy your music")

           elif 'what is the time' in query or 'whats the time' in query or 'what is the time now' in query or 'time now' in query  :
                   time=datetime.datetime.now().strftime("%H:%M:%S")
                   speak("the time is ")
                   engine.say(time)
                   print(time)
                  
               

           elif 'good night' in query or'night' in query or 'sleep time' in query :
                speak("good night")
                speak("Sleep well")
                
                

           elif  'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
                 speak('okay')
                 speak('have a good day.')
                 sys.exit()

           else:
               query=query
               speak('searching....')
               print("searching....")
               try:
                   try:
                       result=client.query(query)
                       results=next(result.results).text
                      # speak('According to wolframalpha')
                       print('According to wolframalpha')
                       print(results)
                       speak(results)
                       
                   except :
                       result=wikipedia.summary(query,sentences=2)
                       print(result)
                       speak(result)
                     
               except:
                   webbrowser.get(chrome).open("www.bing.com")
                   
                  
                   
               
           
                   
               
               
    
    
    