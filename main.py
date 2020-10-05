import os
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time

# настройки
opts = {
    "alias": ("помошник", "слуга" "раб"),
    "tbr": ("скажи", "покажи", "включи", "открой", "запусти"),
    "cmd": {
        "time": ('который час?', 'сколько времени?'),
        "totwar": ("тотал вар", "тотал варыч"),
        "vk": ("вк", "вконтакте", "вэкашка"),
        "youtube": ("ютуб", "ютабчек", "ютубусик"),
        "thunder": ("танки", "танчики", "тундру"),
        "wow": ("вовку", "варик", "вов", "варкрафт", "варкрафтик"),
        "dota": ("дотан", "дотку", "дотку", "доту"),
        "hoi4": ("хойку", "хоечку"),
        "music": ('музон', "музончик", "музыку")
    }

}


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):

            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    rc = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def execute_cmd(cmd):
    if cmd == 'time':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == 'totwar':
        os.system(r"C:\Users\Админ\Desktop\Games from Steam\Total War SHOGUN 2")
    elif cmd == 'thunder':
        os.system(r"C:\Users\Админ\Desktop\Games from Steam\War Thunder")
    elif cmd == 'dota':
        os.system(r"C:\Users\Админ\Desktop\Games from Steam\Dota 2")
    elif cmd == 'hoi4':
        os.system(r"C:\Users\Админ\Desktop\Games from Steam\Hearts of Iron IV")
    elif cmd == 'wow':
        os.system(r"C:\Users\Админ\Desktop\Blizzard games\Legion")
    elif cmd == 'vk':
        webbrowser.open('https://vk.com/feed', new=2)
    elif cmd == 'youtube':
        webbrowser.open('https://www.youtube.com/', new=2)
    elif cmd == "music":
        webbrowser.open('https://vk.com/audios218459683', new=2)
    else:
        print('Команда не распознана, повторите!')


# запуск

r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

speak("Приветствую, Повелитель")
speak("Я готова служить")

stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)
