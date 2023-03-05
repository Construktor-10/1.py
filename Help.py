import speech_recognition as sr
import pyttsx3
import comands

r = sr.Recognizer()
voice = pyttsx3.init()


def Help_start():
    global Help_on
    Help_on = "true"
    voice.say("Открыто меню помощи. -- Здесь можно узнать имеющиеся команды. -- Так-же можно узнать некоторую тех информацию о голосовом помошнике.")
    voice.say("Есть такие команды как КОМАНДЫ для перечисленя имеющихся команд, и ТЕХ-ИНФОРМАЦИЯ для перечисления тех информации о голосовом помошнике")
    Help()

def Help(): 
    global Help_on   
    while Help_on == "true":

        voice.say("Что могу подсказать?")
        voice.runAndWait()

        with sr.Microphone(device_index=0) as source: 
            print("Чем могу помочь?")
            audio = r.listen(source)

        speech = r.recognize_google(audio, language="ru_RU")
        print("Вы сказали " + speech)


        if speech.find("команды") >= 0:
            a = str(comands.comands)
            voice.say("Имеются команды: " + a)
            voice.runAndWait

        #elif speech.find("") >= 0:
        #    voice.say("")
        #    voice.runAndWait
#
        #elif speech.find("") >= 0:
        #    voice.say("")
        #    voice.runAndWait
#
        #elif speech.find("") >= 0:
        #    voice.say("")
        #    voice.runAndWait

        elif speech.find("выход") >= 0:
            Help_on = "off"

        else:
            voice.say("Я вас не понимаю")