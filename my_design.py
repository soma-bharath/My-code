import pyaudio
import speech_recognition as sr
import datetime
import pywhatkit as py
import pyttsx3
import os
import pyjokes
import pyspark
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Go ahead I can hear you..........')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')
  
    except sr.UnknownValueError:
        #print("unable to proceed")
        assistant(myCommand())
    return command
def system_applications(s):
    if "chrome" in s:
        pyttsx3.speak("what would you like to search in chrome")
        z1=myCommand()
        py.search(z1)
    elif "youtube" in s:
        pyttsx3.speak("what would you like to search in youtube")
        z2=myCommand()
        py.playonyt(z2)
    elif "notepad" in s or "editor" in s:
        os.system("notepad")
    elif "player" in s:
        os.system("wmplayer")
    elif "shutdown" in s or "close" in s or "off" in s or "shut" in s:
        os.system("shutdown /s /t 1");
    elif "restart" in s:
        os.system("shutdown /r /t 1");
    elif "photoshop" in s or "edit" in s or "photo" in s:
        os.system("Photoshop")
    elif "whatsapp" in s or "ping" in s or "message" in s:
        number=input("Please enter your friend mobile number: ")
        message_1=input("enter the text that you want to send")
        n1="+91 "+number
        py.sendwhatmsg(n1,message_1,current_time.hour,current_time.minute+4)
    elif "age" in s or "old" in s:
        pyttsx3.speak("I need few details for calculating your age please provide them as mentioned below:")
        year=int(input("Mention the year you born: "))
        month=int(input("Enter the month: "))
        date=int(input("Enter the date: "))
        present_time=datetime.datetime(year,month,date)
        diff=(current_time-present_time).days
        my_age=(diff/365)
        My_Age="You are {} years old".format(int(my_age))
        pyttsx3.speak(My_Age)
    elif "bored" in s or "joke" in s:
        pyttsx3.speak(pyjokes.get_joke())
    else:
        pyttsx3.speak("I regret for the inconvenience caused to you\n So, sorry for it")
    return

current_time=datetime.datetime.now() 
engine = pyttsx3.init()
engine.setProperty('rate', 95)
print("------------------------------------------WELCOME TO PYTHON WORLD------------------------------------")
pyttsx3.speak("Hey hi welcome to my world Myself jarvis")
pyttsx3.speak("will you like to continue with me or you want luci?")
z=myCommand()
if "want" in z:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 95)
    engine.setProperty('voice', voices[1].id)
    pyttsx3.speak("Hey hi welcome to my world Myself Luci")
    pyttsx3.speak("Let me brief you what all I can do for you\n I can open up applications in your system, run videos on youtube, search things in google, send mesaages to friends in whats app\n I can do a lot still")
    pyttsx3.speak("well you can see the list of things being displayed on your screen that i can do for you")
    print("1.Stream youtube\n2.Browse Internet\n3.Shutdown PC\n4.Restart PC\n5.Ping a friend in whats app\n6.Tell your age\n7.Open photo editor\n8.Open text editor\n9.Open window media player\nMANY MORE..............")
    while True:
        
        s=myCommand()
        #s=input("How can I help you?")
        if "done" in s or "bye" in s or "call it a day" in s:
            pyttsx3.speak("Hope you loved the service\n Have a good day\n BYE")
            break
        else:
            system_applications(s)

else:
    #pyttsx3.speak("Let me brief you what all I can do for you\n I can open up applications in your system, run videos on youtube, search things in google, send mesaages to friends in whats app\n I can do a lot of stuff still")
    #pyttsx3.speak("well you can see the list of things being displayed on your screen that i can do for you")
    print("1.Stream youtube\n2.Browse Internet\n3.Shutdown PC\n4.Restart PC\n5.Ping a friend in whats app\n6.Tell your age\n7.Open photo editor\n8.Open text editor\n9.Open window media player\nMANY MORE...............")
    while True:
        print("go on.....")
        s=myCommand()
        #s=input("How can I help you?")
        if "done" in s or "bye" in s or "call it a day" in s:
            pyttsx3.speak("Hope you loved the service\n Have a good day\n BYE")
            print("Take care BYE")
            break
        else:
            system_applications(s)
 









