import speech_recognition as sr
import pyttsx3
import Open_program
import Open_site
import Help


r = sr.Recognizer()
voice = pyttsx3.init()



def Open_start():
    global Open_on
    Open_on = "true"
    Open()

def Open():
    global Open_on
    while Open_on == "true":
        voice.say("Выберете тип открываемого обьекта")
        voice.runAndWait()
        with sr.Microphone(device_index=0) as source: 
            print("Выберете тип открываемого обьекта")
            audio = r.listen(source)
        speech = r.recognize_google(audio, language="ru_RU")
        print("Вы сказали " + speech)

        if speech.find("приложение") >= 0:
            Open_program.Open_program_start()

        elif speech.find("сайт") >= 0:
            Open_site.Open_site_start()

        elif speech.find("помощь") >= 0:
                Help.Help_start()   
                voice.runAndWait()

        elif speech.find("выход") >= 0:
            Open_on = "off"

        else:
            voice.say("Я вас не понимаю")