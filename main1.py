import pyttsx3
import pyaudio
import speech_recognition as sr
import os
import wikipedia
import datetime
import webbrowser
import time
engine = pyttsx3.init()
# engine.say("test")#200 rate default
engine.runAndWait()



# r = sr.Recognizer()

# # Reading Microphone as source
# # listening the speech and store in audio_text variable

# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
#     try:
#         # using google speech recognition
#         print("Text: "+r.recognize_google(audio_text))
#     except:
#          print("Sorry, I did not get that")


rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate
voices = engine.getProperty('voices')      #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
# engine.say("Hello World,yo!")
# engine.say(r.recognize_google(audio_text))
# engine.say('My current speaking rate is ' + str(rate))

# statement=r.recognize_google(audio_text)

r = sr.Recognizer()
k=2
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        engine.say("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        engine.say("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        engine.say("Hello,Good Evening")
        print("Hello,Good Evening")



while True:
    with sr.Microphone() as source:
        print("speak")
        audio_text = r.listen(source)
        statement = r.recognize_google(audio_text)
        print(statement)
    try:
        print("working")
    except:
        engine.say("could you repeat that sir")

    
    if "mute" in statement:
        break
    wishMe()
    if "hello" in statement:
        engine.say("mr.agarwal ,what can i do for you?")
        engine.runAndWait()
        
    if "search on wikipedia" in statement:
        results= wikipedia.summary(statement,sentences=2)
        engine.say(statement)
        engine.runAndWait()
    if "mute" in statement:
        break
    if 'open YouTube' in statement:
            engine.say("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(1)
            engine.runAndWait()
    
    if "open file" in statement:
        qwer = statement.replace('open file','')
        def abc():
            with open(f'{statement}','r') as f:
               a = f.read()
               print(a)
    
        engine.say(a)


    if 'search'  in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(2)
        engine.runAndWait()
    if "who are you" in statement or "what can you do" in statement:
        engine.say("i am mr.agarwal's personal assistant,qwerty. i can do whatever mr. agarwal wants me to do")
        engine.runAndWait()
    answer= " "
    if "find me files in directory" in statement:
        # r = sr.Recognizer()
        engine.say("access denied,please provide password")
        print("speak -2")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio1 = r.listen(source,10,3)
            statement2 = r.recognize_google(audio1)
            print(statement2)

        if "go" in statement2:
            engine.say("which files do you want to see ,sir?")
            engine.runAndWait()
            with sr.Microphone() as source:
                audio2 = r.listen(source,10,3)
                statement3 = r.recognize_google(audio2)
                print(statement3)
                if "all" in statement3:
                    directory_result= os.listdir("C://Program Files (x86)")
                    engine.say("here are the files list.")
                    print(directory_result)
                    engine.say(directory_result)
                    engine.runAndWait()
    if "find me" in statement:
        results1 = os.walk(statement.replace("find file",""))
        # engine.say(os.environ)
        print(os.environ)
        engine.runAndWait()

engine.runAndWait()
engine.stop()