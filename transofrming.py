import os

from pydub import AudioSegment

def convert_audio(input_file, output_file, target_channels=1, target_frame_rate=16000):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_channels(target_channels)
    audio = audio.set_frame_rate(target_frame_rate)
    audio.export(output_file, format="wav")


for file in os.listdir("Source_audio"):
    if file.endswith(".m4a") or file.endswith(".mp3") or file.endswith(".wav"):
        input_file = "Source_audio/" + file
        output_file = "Res_audio/" + file[:-4] + ".wav"
        convert_audio(input_file, output_file)
