import os

import speech_recognition as sr


def whisper_to_text(audio_file):
    def write_to_file(input_string, file_name):
        words = input_string.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) <= 80:
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = word + " "

        if current_line:
            lines.append(current_line)

        with open("Source_translate/" + file_name, 'w') as file:
            for line in lines:
                file.write(line + "\n")

    # Создаем объект Recognizer, включающий в себя API Whisper
    recognizer = sr.Recognizer()
    # Открываем аудиофайл и записываем данные из него
    with sr.AudioFile("Res_audio/" + audio_file) as source:
        audio_data = recognizer.record(source)

    # Распознаем текст в аудио
    try:
        text = recognizer.recognize_whisper(audio_data, language="en")
        print("Текст из аудиофайла: {}".format(text))
        write_to_file(text, audio_file[:-4] + ".txt")
    except sr.UnknownValueError:
        print("Речь не распознана")
    except sr.RequestError:
        print("Не удалось выполнить запрос к сервису распознавания речи")


def write_long(long_string, file_name):
    with open(file_name, 'w') as file:
        # Разбиваем длинную строку на строки длиной 80 символов
        lines = [long_string[i:i + 80] for i in range(0, len(long_string), 80)]
        # Записываем строки в файл
        for line in lines:
            file.write(line + '\n')


for file in os.listdir("Res_audio/"):
    print(file)
    if file.endswith(".wav"):
        audio_file = file
        print(audio_file)
        whisper_to_text(audio_file)