'''Prerequest:-
1.Make sure latest Microsoft Visual C++ Build Tools is installed in your pc.  (link:-https://go.microsoft.com/fwlink/?LinkId=691126)
2.Please run  this command  as well:-pip install port audio
3.To get weather feature work ,you have to create your own  api key from here 'https://openweathermap.org/api'
'''
#All imported packages  are below
import  pyttsx3 #Important:-Always install this  package through this command to avoid errors - pip install -Iv pyttsx3==2.6 -U
import datetime #pip install datetime
import calendar #pip install calender
import speech_recognition as sr  #pip install SpeechRecognition
import pyaudio  #(For microphone user) pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl (link to download .whl file :- https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
import wikipedia
import webbrowser
import sysconfig
import os
import glob
import requests


#Coding start from here
operating_system = sysconfig.get_platform().split("-")
if operating_system[0] == 'win':
    engine = pyttsx3.init("sapi5") #pyttsx is used to convert text-to-speech
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)    # 1 for female voice and 0 of male voice


def months(audio):
    number_to_month = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
    }
    today = ['current month','today month','which month is this']
    tomorrow = ['next month','month next','which is the next month']
    yestarday = ['previous month','month previous','which was the previous month']
    print(audio)
    if audio in today:
        print(f"Currently it's {number_to_month.get(int(datetime.datetime.now().month))}")
        engine.say(f"Currently it's {number_to_month.get(int(datetime.datetime.now().month))}")
        engine.runAndWait()
        listen()
    elif audio in tomorrow:
        print(f'Next month is {number_to_month.get(int(datetime.datetime.now().month) + 1 )} ')
        engine.say(f'Next month is {number_to_month.get(int(datetime.datetime.now().month) + 1 )}')
        engine.runAndWait()
        listen()
    elif audio in yestarday:
        print(print(f'Previously it was {number_to_month.get(int(datetime.datetime.now().month)-1)}'))
        speak(f'Previously it was  {number_to_month.get(int(datetime.datetime.now().month) - 1 )}')
        listen()
    else:
        listen()


def time():
    formate_to_standard = {
        '01':1,
        '02':2,
        '03':3,
        '04':4,
        '05':5,
        '06':6,
        '07':7,
        '08':8,
        '09':9,
        '10':10,
        '11':11,
        '12':12,
        '13':1,
        "14":2,
        "15":3,
        "16":4,
        "17":5,
        "18":6,
        "19":7,
        "20":8,
        "21":9,
        "22":10,
        "23":11,
        "24":12
    }
    time = str(datetime.datetime.now().time())
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        value = 'AM'
    else:
        value = 'PM'
    standard_time = time.split(":")
    print(f"It's {formate_to_standard.get(standard_time[0])}{standard_time[1]} {value}")
    engine.say(f"It's {formate_to_standard.get(standard_time[0])}{standard_time[1]} {value}")
    engine.runAndWait()
    listen()


def hello():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        print(f"Hello\nGood Morning\n"
              f"how may help you?")
        engine.say(f"Hello,Good Morning"
                   f"how ,may help you")
        engine.runAndWait()
        listen()
    elif hour>=12 or hour <= 17:
        print(f"Hello\nGood Afternoon\n"
              f"how may help you?")
        engine.say(f"Hello Good Afternoon"
                   f"how may help you?")
        engine.runAndWait()
        listen()
    elif hour > 17:
        print(f'Hello Good Evening')
        print(f"Hello\nGood Evening\n"
              f"how may help you?")
        engine.say(f"Hello Good Afternoon"
                   f"how may help you?")
        engine.runAndWait()
        listen()


def callendar(audio):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    months_to_number = {
        'January':1,
        'February':2,
        'March':3,
        'April':4,
        'May':5,
        'June':6,
        'July':7,
        'August':8,
        'September':9,
        'October':10,
        'November':11,
        'December':12,

    }
    values = audio.split(' ')
    for value in values:
        if value in months:
            engine.say('Here is the result')
            print(calendar.month(int(values[-1]),int(months_to_number.get(value))))
            engine.runAndWait()
            listen()


def operation(audio):
    class Calculation:
        def __init__(self,n):
            self.n = n
        def __add__(self, other):
            return self.n + other.n
        def __sub__(self, other):
            return  self.n - other.n
        def __mul__(self, other):
            return  self.n * other.n
    values = audio.split(" ")
    symbol_to_value = {
        'multiply':'*',
        'divide':'/'
    }
    if symbol_to_value.get(values[2]):
        symbol = symbol_to_value.get(values[2])
    elif symbol_to_value.get(values[2]):
        symbol = symbol_to_value.get(values[2])
    else:
        symbol = values[2]
    x = Calculation(int(values[1]))
    y = Calculation(int(values[3]))
    if symbol == '+':
        result = x + y
        print(result)
        engine.say(result)
        engine.runAndWait()
        listen()
    elif symbol == '-':
        result = x - y
        print(result)
        engine.say(result)
        engine.runAndWait()
        listen()
    elif symbol == '*':
        result = x * y
        print(result)
        engine.say(result)
        engine.runAndWait()
        listen()
    elif symbol == '/':
        x = int(values[1])
        y = int(values[3])
        result = x / y
        print(result)
        engine.say(result)
        engine.runAndWait()
        listen()
    else:
        print('Wrong Input')
        engine.say('Wrong Input')
        engine.runAndWait()
        listen()


def wiki(audio):
    print(wikipedia.summary(audio,sentences=2))
    engine.say(wikipedia.summary(audio,sentences=2))
    engine.runAndWait()
    listen()


def date(audio):
    print(f'Today is {datetime.datetime.now().date()}')
    engine.say(f'Today is {datetime.datetime.now().date()}')
    engine.runAndWait()
    listen()


def window(audio):
    if audio.endswith('.com'):
        values = audio.split(" ")
        print(f'Opening {values[1]}')
        engine.say(f'Opening{values[1]}')
        webbrowser.open(f'www.{values[1]}')
        engine.runAndWait()
    else:
        values = audio.split(" ")
        print(f'Opening {values[1]}')
        engine.say(f'Opening{values[1]}')
        webbrowser.open(f'www.{values[1]}.com')
        engine.runAndWait()




def weather(audio):
    values = audio.split(' ')
    city = values[-1].lower()
    key = ''  #Put your api key here into the string
    if key:
        url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}'
        data = requests.get(url).json()
        weather = data['weather'][0]['main']
        temp_in_kelvin = data['main']['temp']
        tem_in_celius = float(temp_in_kelvin) - 273.15
        wind = data['wind']['speed']

        print(f'Currently in {city} weather is {weather}')
        engine.say(f'Currently in {city} weather is {weather}')
        engine.runAndWait()
        print(f'Currently in {city} tempeature is {round(tem_in_celius)} in celsius')
        engine.say(f'Currently in {city} tempeature is {round(tem_in_celius)} in celsius')
        engine.runAndWait()
        print(f'Currently in {city} speed of wind is  {round(wind*1.609344)} km/h')
        engine.say(f'Currently in {city} speed of wind is  {round(wind*1.609344)} km/h')
        engine.runAndWait()
    else:
        print('''
Disclaimer:-Generally  to avoid  security issue it is always a good pratice not to put 
your own  key online directly ,to get your own key please follow the steps :-
1.Go to https://openweathermap.org/
2.Sign up for a free user account
3.go to API Tab and get your free apis for free or you can choose the subscriptions plan 
4.once all the above steps are done ,put your key into key.py file .
        ''')
        print('Do you want me to redirect to the page url? say Yes or No')






def changevoice(audio):
    value = audio.split(' ')[-1]
    if value == 'male':
        engine.setProperty('voice',voice[0].id)
        print('Changed has been done sucessfully')
        engine.say('Changed has been done sucessfully')
        engine.runAndWait()
        listen()
    else:
        engine.setProperty('voice',voice[1].id)
        print('Changed has been done sucessfully')
        engine.say('Changed has been done sucessfully')
        engine.runAndWait()
        listen()


def speak(audio):
    if 'month' in audio:
        months(audio)

    elif 'time' in audio:
        time()

    elif 'hello' in audio:
        hello()

    elif 'calendar' in audio:
        callendar(audio)

    elif 'calculate' in audio:
        operation(audio)

    elif 'Wikipedia' in audio:
        wiki(audio)

    elif 'date' in audio:
        date(audio)

    elif 'change voice to' in audio:
        changevoice(audio)


    elif "what's the weather like in" in audio:
        weather(audio)

    elif audio in ["how are you"]:
        print("I'm Good, \n how may I help you ")
        engine.say("I'm Good,\n How may I help you")
        engine.runAndWait()
        listen()

    elif 'open' in audio:
        window(audio)

    elif audio in ['bye','tata']:
        print('Byee !')
        engine.say('Bye')
        engine.runAndWait()

    else:
        print(audio)
        engine.say(audio)
        engine.runAndWait()


def listen():
    '''#This below code is basically listen your voice with the microphone then convert the auido into string
    ##Sample rate is how often values are recorded
    #Chunk is like a buffer. It stores 2048 samples (bytes of data) here.it is advisable to use powers of 2 such as 1024 or 2048
    '''
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=48000,chunk_size=2048) as source:
        print('Listening...')
        r.energy_threshold = 100 #If you're having trouble with the recognizer trying to recognize words even when you're not speaking, try tweaking this to a higher value. If you're having trouble with the recognizer not recognizing your words when you are speaking, try tweaking this to a lower value.
        audio = r.listen(source,timeout=4,phrase_time_limit=4)  # other than source this other to make it stop and return after a certain number of seconds even if no speech or silence have been detected
    try:
        #Now with this code the  audio will be process with the help of google recognize function then we call speak method
        print('Searching...')
        value = r.recognize_google(audio,language="en-in") #this method  will convert audio into text ,internet connection is requires
        speak(value)
    except:
        print("I didn't get it please say it again")
        speak("I didn't get it please say it again")
        return 'None'


listen()

