import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import File_creator
import Open


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
        Open()
        
    elif speech.find("создай") >= 0:
        File_creator()

    elif speech.find("дата") >= 0:
            today = datetime.today()
            today = today.strftime('%d/%m/%Y')
            voice.say(today)
            voice.runAndWait()

    elif speech.find("помощь") >= 0:
            voice.say("Имеются команды")
            voice.say("дата для определения даты") 
            voice.say("создай для создания папки")  
            voice.say("открой для открытия ютуба")   
            voice.say("и пока для закрытия программы")    
            voice.runAndWait()

    elif speech.find("пока") >= 0:
        voice.say("До встречи")
        voice.runAndWait()
        break
    #Если ничего не нащёл
    else:
        voice.say("Я вас не понимаю")
        voice.runAndWait()