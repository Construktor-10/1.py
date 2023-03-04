import speech_recognition as sr
import pyttsx3
import os


r = sr.Recognizer()
voice = pyttsx3.init()


Open_program_on = True
while Open_program_on == True:
    voice.say("Выберете приложение")
    voice.runAndWait()
    with sr.Microphone(device_index=0) as source:
        print("Выберете приложение")
        audio = r.listen(source)
    speech = r.recognize_google(
        audio, language="ru_RU")
    print("Вы сказали " + speech)

if speech.find("браузер") >= 0:
    os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
    voice.say("Браузер открыт")

# elif speech.find("") >= 0:
#    os.startfile("")
#    voice.say("")
#
# elif speech.find("") >= 0:
#    os.startfile("")
#    voice.say("")

elif speech.find("выход") >= 0:
        Open_program_on = False
else:
    voice.say("Я вас не понимаю")