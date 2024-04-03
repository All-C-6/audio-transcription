import speech_recognition as sr

# Создаем объект Recognizer
recognizer = sr.Recognizer()

# Загрузка звукового файла в формате .wav
audio_file = "Source_audio/output.wav"

# Загрузка файла
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
    recognizer.adjust_for_ambient_noise(source)

# Попытка распознавания речи на русском языке с помощью Sphinx
try:
    print(recognizer.recognize_google(audio, language="ru-RU"))
except sr.UnknownValueError:
    print("Извините, не удалось распознать речь")
except sr.RequestError as e:
    print("Извините, ошибка сервиса; {0}".format(e))