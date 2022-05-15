import os

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb

opts = {
    "alias": ('луна', 'louna', 'лун', 'ассистент'),
    "hello": ('дела', 'настроение'),
    "tbr": ('скажи', 'расскажи', 'сколько','как'),
    "find": ('загугли'),
    "help": ('умеешь'),
    "to_open0": ('телеграм', 'telegram', 'телегу'),
    "to_open1": ('браузер', 'интернет', 'брэйв')
}


def telega():
    os.startfile(r'C:\Users\37533\AppData\Roaming\Telegram Desktop\Telegram.exe')


def browser():
    os.startfile(r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe')


def speak(text):
    print(text)
    tts.say(text)
    tts.runAndWait()
    tts.stop()


def hellower():
    speak('Всё прекрасно, знаю и у вас всё хорошо')


def help_first():
    speak(
        'Я могу сказать который час,гуглить могу... Шуток не знаю и пока не могу писать заметки, но босс это исправит')


def callback(voice):
    if voice.startswith(opts["alias"]):
        cmd = voice

        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

        return execute_cmd(cmd)


def todo_list():
    speak('Что добавить?')
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        query = r.recognize_google(audio_data=audio,language='ru-RU').lower()

    with open('todo_list.txt','a') as list_d:
        list_d.write(f'{query}\n')
    return speak('Добавила')

def execute_cmd(cmd):
    print(cmd)
    if cmd == 'время':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif 'заметка' in cmd.split():
        todo_list()
    elif opts["find"] in cmd.split():
        cmd = cmd.replace(opts["find"], "").strip()
        wb.open('http://www.google.com/search?q=' + cmd)
        speak('Вот что я нашла')
    elif cmd in opts["to_open0"]:
        telega()
    elif cmd in opts["to_open1"]:
        browser()
    elif opts["help"] in cmd.split():
        help_first()
    elif cmd in opts["hello"]:
        hellower()
    else:
        print('Команда не распознана, повторите!')


def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1)
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышалa.')
    try:
        query = r.recognize_google(audio, language='ru-RU').lower()
        text = query.lower()
        print(f'Вы сказали: {text}')
        return callback(text)
    except:
        print('Error')


tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
ttm = datetime.datetime.now()
if ttm.hour <= 12 and ttm.hour >= 6:
    speak('Доброго утречка')
elif ttm.hour > 12 and ttm.hour <= 17:
    speak('Добрый день')
elif ttm.hour > 17 and ttm.hour <= 23:
    speak('Доброго вечера')
else:
    speak('Доброй ночи')

while True:
    record_volume()
    if record_volume() == "стоп":
        break
