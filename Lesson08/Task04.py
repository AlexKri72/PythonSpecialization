# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import os
import json


def func(file_in, file_out):
    '''Читаем csv файл, переделываем и записываем в json.'''

    json_out = []
    if os.path.isfile(file_in) and 0 < os.path.getsize(file_in):
        with open(file_in, 'r', newline='', encoding='utf-8') as f:
            f_in = csv.reader(f)
            for num, row in enumerate(f_in):
                json_dict = {}
                if num != 0:
                    level, user_id, name = row
                    json_dict['level'] = int(level)
                    json_dict['user_id'] = user_id.zfill(10)
                    json_dict['name'] = name.lower()
                    json_dict['hash'] = hash(f'{name}{user_id}')
                    json_out.append(json_dict)
    with open(file_out, 'w', encoding='utf-8') as f_out:
        json.dump(json_out, f_out, indent=4)


if __name__ == '__main__':
    func('Task03.csv', 'Task04.json')
