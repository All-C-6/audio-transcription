import time
import wave
import vosk

output_wav_file = "Source_audio/output_file.wav"

# Загрузка модели для распознавания
model = vosk.Model("/home/all_c/dophamine/Vosk/Model/vosk-model-en-us-0.22")

start_time = time.time()
# Открытие аудиофайла
wf = wave.open("Res_audio/auditboard.wav", "rb")
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
with open('Source_translate/185ep.txt', 'w') as file:
    for item in result:
        file.write(str(item) + '\n')

end_time = time.time()
print("Время распознавания: " + str(end_time - start_time))
