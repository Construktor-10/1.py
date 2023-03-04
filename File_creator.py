import speech_recognition as sr
import File_creator_directory
import File_creator_txt
import pyttsx3

r = sr.Recognizer()
voice = pyttsx3.init()


def File_creator():
    file_creator_on = "true"
    while file_creator_on == "true":

        voice.say("Выберете тип файла")
        voice.runAndWait()

        with sr.Microphone(device_index=0) as source_for_file_creator: 
            print("Выберете тип файла")
            audio_for_file_creator = r.listen(source_for_file_creator)

        speech_for_file_creator = r.recognize_google(audio_for_file_creator, language="ru_RU")
        print("Вы сказали " + speech_for_file_creator)

        
        if speech_for_file_creator.find("директория") >= 0:
            File_creator_directory()

        if speech_for_file_creator.find("текст") >= 0:
            File_creator_txt()


        elif speech_for_file_creator.find("выход") >= 0:
            file_creator_on = "off"
            
        else:
            voice.say("Я вас не понимаю")