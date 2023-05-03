# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import pickle
import os


def json_to_pickle(curren_dir):
    '''Ищем в директории json файлы, читаем и пишем pickle файлы с таким же именем.'''

    for file in os.listdir(curren_dir):
        if file.split('.')[1] == 'json':
            with (
                open(file, 'r', encoding='utf-8') as f,
                open(f'{file.split(".")[0]}.pickle', 'wb') as f_pickle
            ):
                f_in = json.load(f)
                pickle.dump(f_in, f_pickle)


if __name__ == '__main__':
    json_to_pickle(os.getcwd())
