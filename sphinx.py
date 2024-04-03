from pocketsphinx import AudioFile, Decoder, Config
import pocketsphinx
import time


config = Config()
config.set_string('-hmm', 'Model/cmusphinx-ru-5.2') # путь к директории с акустической моделью
config.set_string('-lm', 'Model/cmusphinx-ru-5.2/ru.lm') # путь к файлу языковой модели
config.set_string('-dict', 'Model/cmusphinx-ru-5.2/ru.dic') # путь к файлу словаря
config.set_string('-kws_threshold', '1e-3') # порог вероятности слова
#config.set_string('-infile', 'SucTry5.wav') # путь к аудиофайлу

decoder = Decoder(config, samprate=16000)
#decoder.get_prob('prob_threshold', 1e-7)  # Пример установки порога вероятности слова
# Чтение аудиофайла
audio_file = 'Source_audio/output.wav'
start_time = time.time()
# Открываем файл и передаем его в Decoder
decoder.start_utt()
stream = open(audio_file, 'rb')
while True:
    buf = stream.read(8000)
    if buf:
        decoder.process_raw(buf)
    else:
        break
decoder.end_utt()

# Получаем результат распознавания
hypothesis = decoder.hyp()

print('Результат:', hypothesis.hypstr)
end_time = time.time()
print("Время распознавания: " + str(end_time - start_time))