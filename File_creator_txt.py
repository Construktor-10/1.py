import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()
voice = pyttsx3.init()


def File_creator_txt():
    voice.say("выберете имя текстового файла")
    voice.runAndWait()
    file_creator_txt_creator = "on"
    while file_creator_txt_creator == "on" :
        with sr.Microphone(device_index=0) as source_for_file_creator_txt_name_chose: 
                print("Скажи имя файла")
                audio_for_file_creator_txt_creator = r.listen(source_for_file_creator_txt_name_chose)

        speech_for_file_creator_txt_creator = r.recognize_google(audio_for_file_creator_txt_creator, language="ru_RU")
        print("Вы сказали "  speech_for_file_creator_txt_creator)

        name = speech_for_file_creator_txt_creator
        try:
            os.mkdir(name)
            voice.say("Тестовый фаил с именем "  name  " создан")
            file_creator_txt_creator = "off"
        except FileExistsError:
            voice.say("Фаил уже существует, создать не возможно")
            file_creator_txt_creator = "off"
        except PermissionError:
            voice.say("Программе отказано в доступе, создать не возможно")
            file_creator_txt_creator = "off"