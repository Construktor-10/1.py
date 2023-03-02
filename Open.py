import speech_recognition as sr
import pyttsx3
import Open_program
import Open_site


r = sr.Recognizer()
voice = pyttsx3.init()

def Open():
    Open_on = "true"
    while Open_on == "true":

        voice.say("Выберете тип открываемого обьекта")
        voice.runAndWait()

        with sr.Microphone(device_index=0) as source_for_Open: 
            print("Выберете тип открываемого обьекта")
            audio_for_Open = r.listen(source_for_Open)

        speech_for_Open = r.recognize_google(audio_for_Open, language="ru_RU")
        print("Вы сказали "  speech_for_Open)

        
        #if speech_for_Open.find("приложение") >= 0:
        #    Open_program()

        if speech_for_Open.find("сайт") >= 0:
            Open_site()


        elif speech_for_Open.find("выход") >= 0:
            Open_on = "off"
            
        else:
            voice.say("Я вас не понимаю")