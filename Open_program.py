import speech_recognition as sr
import pyttsx3
import os


r = sr.Recognizer()
voice = pyttsx3.init()

def Open_program():
    Open_program_on = "true"
    while Open_program_on == "true":

        voice.say("Выберете приложение")
        voice.runAndWait()

        with sr.Microphone(device_index=0) as source_for_Open_program: 
            print("Выберете приложение")
            audio_for_Open_program = r.listen(source_for_Open_program)

        speech_for_Open_program = r.recognize_google(audio_for_Open_program, language="ru_RU")
        print("Вы сказали "  speech_for_Open_program)    

    if speech.find("браузер") >= 0:
        os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
        voice.say("Браузер открыт")
        Open_program_on = "off"

    elif speech.find("") >= 0:
        os.startfile("")
        voice.say("")
        Open_program_on = "off"

    elif speech.find("") >= 0:
        os.startfile("")
        voice.say("")
        Open_program_on = "off"
            
    else:
        voice.say("Я вас не понимаю")