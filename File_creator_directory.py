import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()
voice = pyttsx3.init()



def File_creator_directory_start():
    global file_creator_directory_creator
    file_creator_directory_creator = "on"
    File_creator_directory()

def File_creator_directory(): 
      
    global file_creator_directory_creator

    voice.say("выберете имя директории")
    voice.runAndWait() 

    while file_creator_directory_creator == "on":
        with sr.Microphone(device_index=0) as source_name_chose:
            print("Скажи имя файла")
            audio = r.listen(
                source_name_chose)

        speech = r.recognize_google(
            audio, language="ru_RU")
        print("Вы сказали " + speech)

        name = speech
        try:
            os.mkdir(name)
            voice.say("Папка с именем " + name + " создана")
            file_creator_directory_creator = "off"

        except FileExistsError:
            voice.say("Фаил уже существует, создать не возможно")
            file_creator_directory_creator = "off"

        except PermissionError:
            voice.say("Программе отказано в доступе, создать не возможно")
            file_creator_directory_creator = "off"
