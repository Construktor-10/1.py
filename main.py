import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import File_creator
import Open
import Help


r = sr.Recognizer()
voice = pyttsx3.init()



voice.say("Привет я голосовой помошник")
voice.runAndWait()
list_hi = ["Привет" , "Hello" , "Приветики" , "здравствуй" , "Хэй"]

while True:
    with sr.Microphone(device_index=0) as source: 
        print("Скажи что-нибуть...")
        audio = r.listen(source)

    speech = r.recognize_google(audio, language="ru_RU")
    print("Вы сказали " + speech)

    if speech.find("привет") >= 0 or speech.find("хай") >= 0 or speech.find("здравствуй") >= 0:
        voice.say(random.choice(list_hi))
        voice.runAndWait()

    #Поиск команд

    elif speech.find("открой") >= 0:
        Open.Open_start()
        voice.runAndWait()
        
    elif speech.find("создай") >= 0:
        File_creator.File_creator_start()
        voice.runAndWait()
        
    elif speech.find("праздник") >= 0 or speech.find("празник") >= 0:

        voice.say("Поздравляю Юлию Липскую с восьмым марта. - - И праздником всех женщин.")

        voice.runAndWait()

    elif speech.find("дата") >= 0:
            today = datetime.today()
            today = today.strftime('%d/%m/%Y')
            voice.say(today)
            voice.runAndWait()

    elif speech.find("помощь") >= 0:
            Help.Help_start()   
            voice.runAndWait()

    elif speech.find("пока") >= 0:
        voice.say("До встречи")
        voice.runAndWait()
        break
    #Если ничего не нащёл
    else:
        voice.say("Я вас не понимаю")
        voice.runAndWait()
