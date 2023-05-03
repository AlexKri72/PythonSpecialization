# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json


def json_trans():
    '''Переводим текст в формат JSON и записываем в файл.'''

    with (
        open('../Lesson07/Task03.txt', 'r', encoding='utf-8') as f_in,
        open('Task01.json', 'w', encoding='utf-8') as f_out
    ):
        data = {}
        for line in f_in:
            name, number = line.split(" ")
            data[name.capitalize()] = float(number)

        json.dump(data, f_out, indent=2)


if __name__ == '__main__':
    json_trans()
