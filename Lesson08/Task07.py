# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.
import os
import pickle
import csv


def read_csv(file):
    '''Читаем csv файл и печатаем как pickle строку'''

    if os.path.isfile(file) and 0 < os.path.getsize(file):
        with open(file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            all_data = []
            for i, val in enumerate(csv_file):
                dict1 = {}
                if not i:
                    keys = val
                else:
                    for j in range(len(keys)):
                        dict1[keys[j]] = val[j]
                all_data.append(dict1)
        all_data.pop(0)
        print(all_data)
        print(pickle.dumps(all_data))


if __name__ == '__main__':
    read_csv('Task06.csv')
