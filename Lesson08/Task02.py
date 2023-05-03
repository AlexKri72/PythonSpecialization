# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import os
from pathlib import Path


def safe_user_data(file: Path) -> None:
    '''Накапливаем в файле введенные пользователем данные авторизации.'''

    global all_id
    all_id = set()
    json_data = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_data = json.load(js)

    all_id.update(*((value.keys()) for value in json_data.values()))

    while True:
        user_id, name, user_level = input(
            "Введите через пробел 'Личный номер','Имя','Уровень доступа (1-7)':  ").split()
        if user_id in all_id:
            print("Такой id уже есть.")
            continue
        elif 1 <= int(user_level) <= 7:
            json_data[user_level][user_id] = name
            with open(file, 'w+', encoding='utf-8') as f:
                print(json_data)
                json.dump(json_data, f, indent=2)
        else:
            print('Неправильно указан уровень доступа!')


if __name__ == '__main__':
    safe_user_data(Path('Task02.json'))
