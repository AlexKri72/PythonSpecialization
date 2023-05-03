# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json
import csv
import os


def safe_json_to_csv(file_name_in):
    '''Читаем файл в формате json и записываем в формате csv.'''

    if os.path.isfile(file_name_in) and 0 < os.path.getsize(file_name_in):
        with open(file_name_in, 'r', encoding='utf-8') as js:
            json_file = json.load(js)
            print(json_file)

    rows = []
    for id_level, value in json_file.items():
        for user_id, name in value.items():
            rows.append([id_level, user_id, name])

    with open('Task03.csv', 'w', newline='', encoding='utf-8') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(['level', 'user_id', 'name'])
        writer.writerows(rows)


if __name__ == '__main__':
    safe_json_to_csv('Task02.json')
