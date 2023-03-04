import speech_recognition as sr
import pyttsx3
import webbrowser


r = sr.Recognizer()
voice = pyttsx3.init()

def callable():
    Open_site_on = "true"
    while Open_site_on == "true":

        voice.say("Выберете сайт")
        voice.runAndWait()

        with sr.Microphone(device_index=0) as source_for_Open_site: 
            print("Выберете сайт")
            audio_for_Open_site = r.listen(source_for_Open_site)

        speech = r.recognize_google(audio_for_Open_site, language="ru_RU")
        print("Вы сказали " + speech)

        
        if speech.find("youtube") >= 0 or speech.find("YouTube") >= 0:
            webbrowser.open_new("https://www.youtube.com/")
            voice.say("Ютуб запущен")
            Open_site_on = "off"

        elif speech.find("google") >= 0:
            webbrowser.open_new("https://www.google.ru/")
            voice.say("Гугл запущен")
            Open_site_on = "off"

        elif speech.find("переводчик") >= 0:
            webbrowser.open_new("https://translate.google.com/?hl=ru")
            voice.say("Переводчик запущен")
            Open_site_on = "off"

            
        else:
            voice.say("Я вас не понимаю")