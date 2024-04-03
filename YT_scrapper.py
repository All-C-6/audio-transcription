from pytube import YouTube

# Вставь URL YouTube видео сюда
video_url = "https://www.youtube.com/watch?v=kThC8ZEu7lo"

# Создаем объект YouTube
yt = YouTube(video_url)

# Выбираем только аудиопоток
audio = yt.streams.filter(only_audio=True).first()

# Получаем первые 30 символов названия видео
video_title = yt.title[:30] + ".m4a"

# Скачиваем аудио файл с именем, основанным на названии видео
audio.download(output_path='Source_audio', filename=video_title)

print("Аудиодорожка успешно загружена!")