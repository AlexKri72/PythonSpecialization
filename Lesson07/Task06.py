# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from Task05 import new_make_file
import os
from pathlib import Path


def generate_to_directory(directory: str, dict1: dict):
    '''генерируем файлы в указанную директорию'''

    if not Path(directory).exists():
        os.mkdir(directory)
    os.chdir(directory)
    new_make_file(dict1)


if __name__ == '__main__':
    generate_to_directory('Task06', {'txt': 2, 'doc': 2, 'xls': 2})
