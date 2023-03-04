import speech_recognition as sr
import File_creator_directory
import File_creator_txt
import pyttsx3

r = sr.Recognizer()
voice = pyttsx3.init()



file_creator_on = "true"
while file_creator_on == "true":

    voice.say("Выберете тип файла")
    voice.runAndWait()

    with sr.Microphone(device_index=0) as source: 
        print("Выберете тип файла")
        audio = r.listen(source)

    speech = r.recognize_google(audio, language="ru_RU")
    print("Вы сказали " + speech)

        
    if speech.find("директория") >= 0:
        File_creator_directory
        
    if speech.find("текст") >= 0:
        File_creator_txt


    elif speech.find("выход") >= 0:
        file_creator_on = "off"
            
    else:
        voice.say("Я вас не понимаю")