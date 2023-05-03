# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv
import os


def pickle_to_csv(file):
    '''Читаем из pickle файла, пишем в csv файл'''

    if os.path.isfile(file) and 0 < os.path.getsize(file):
        with (
            open(file, 'rb') as f,
            open('Task06.csv', 'w', newline='', encoding='utf-8') as f_out
        ):
            pickle_file = pickle.load(f)
            csv_file = csv.writer(f_out)
            csv_file.writerow(pickle_file[0].keys())

            for i in pickle_file:
                row = []
                for j in pickle_file[0].keys():
                    row.append(i[j])
                csv_file.writerow(row)


if __name__ == '__main__':
    pickle_to_csv('Task04.pickle')
