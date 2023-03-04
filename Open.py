import speech_recognition as sr
import pyttsx3
import Open_program
import Open_site


r = sr.Recognizer()
voice = pyttsx3.init()

Open_on = "true"
while Open_on == "true":
    voice.say("Выберете тип открываемого обьекта")
    voice.runAndWait()
    with sr.Microphone(device_index=0) as source: 
        print("Выберете тип открываемого обьекта")
        audio = r.listen(source)
    speech = r.recognize_google(audio, language="ru_RU")
    print("Вы сказали " + speech)
    
    if speech.find("приложение") >= 0:
        Open_program

    if speech.find("сайт") >= 0:
        Open_site
        
    elif speech.find("выход") >= 0:
        Open_on = "off"
        
    else:
        voice.say("Я вас не понимаю")