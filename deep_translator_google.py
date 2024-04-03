import os

from deep_translator import GoogleTranslator


def translating(txt_raw_file):
    # Чтение содержимого из исходного файла
    file_path = 'Source_translate/'
    with open(file_path + txt_raw_file, 'r', encoding='utf-8') as file:
        text_to_translate = file.read()

    # Перевод текста с помощью Google Translate через Deep-Translator
    translated_text = GoogleTranslator(source='auto', target='ru').translate(text_to_translate)

    # Запись переведенного текста в новый файл
    output_file_path = 'Res_translate/' + txt_raw_file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print("Текст успешно переведен и записан в output.txt!")


for file in os.listdir("Source_translate"):
    if file.endswith(".txt"):
        translating(file)