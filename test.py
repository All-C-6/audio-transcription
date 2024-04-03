import time
import wave

import ffmpeg
import vosk
from pydub import AudioSegment


def mp3_to_wav(input_file="SucTry5.wav", output_file="output_file.wav", sample_rate=16000, channels=1):
    # Загружаем mp3 файл
    sound = AudioSegment.from_mp3(input_file)

    # Преобразуем в нужные параметры: sample_rate и channels
    sound = sound.set_frame_rate(sample_rate).set_channels(channels)

    # Сохраняем как wav файл
    sound.export(output_file, format="wav")

# Указываем пути к вашим файлам
input_mp3_file = "input_file.mp3"
output_wav_file = "Source_audio/output_file.wav"

# Вызываем функцию с нужными характеристиками (пример: sample_rate=44100, channels=2)
mp3_to_wav()

# Загрузка модели для распознавания
model = vosk.Model("/home/all_c/dophamine/Vosk/Model/vosk-model-ru-0.22")

start_time = time.time()
# Открытие аудиофайла
wf = wave.open("Source_audio/output_file.wav", "rb")
print("Размер аудиофайла: " + str(wf.getnframes()))
# Создание объекта для распознавания
recognizer = vosk.KaldiRecognizer(model, wf.getframerate())

# Чтение данных из аудиофайла и распознавание
result = []
while True:
    data = wf.readframes(32000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result.append(recognizer.Result()[14:-3])


# Получение окончательного результата
print("Результат: ")
print(result)

end_time = time.time()
print("Время распознавания: " + str(end_time - start_time))
