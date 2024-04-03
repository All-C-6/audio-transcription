import os

from deep_translator import GoogleTranslator


def translating(txt_raw_file):
    def barrier(wordlist):
        total_length = 0
        words_num = 0

        for word in wordlist:
            if total_length + len(word) <= 5000:
                words_num += 1
                total_length += len(word) + 1
            else:
                break
        return words_num

    def read_all_words_from_file(file_name):
        words = []

        with open(file_name, 'r') as file:
            for line in file:
                # Разделение строки на слова с использованием пробела как разделителя
                line_words = line.split()
                words.extend(line_words)

        return words

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

        with open("Res_translate/" + file_name, 'w') as file:
            for line in lines:
                file.write(line + "\n")


    file_path = 'Source_translate/' + txt_raw_file  # замените 'example.txt' на путь к вашему файлу
    resulting_words = read_all_words_from_file(file_path)
    words = ""
    start = 0
    end = barrier(resulting_words[start:]) - 1
    print(f"Начало: {start} и конец: {end}")
    print(resulting_words)
    print(f"Тип данных: {type(resulting_words)}\nКоличество слов: {len(resulting_words)}")

    # Перевод текста с помощью Google Translate через Deep-Translator
    while True:
        translated = (GoogleTranslator(source='auto', target='ru').translate(" ".join(resulting_words[start:end])))
        print(f"Перевод: {translated}")
        print(f"Оригинал: {' '.join(resulting_words[start::end])}")
        words += translated
        start = end
        end = start + int(barrier(resulting_words[start:])) - 1
        print(f"Начало: {start} и конец: {end}")
        print(f"Элемент начала: {resulting_words[start]} и элемент конца: {resulting_words[end]}")
        print(resulting_words[start])
        if end + 1 == len(resulting_words):
            print("Работа завершена")
            break

    write_to_file(words, txt_raw_file)


for file in os.listdir("Source_translate"):
    if file.endswith(".txt"):
        translating(file)
