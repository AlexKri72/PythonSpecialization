# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,  состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice, randint
from pathlib import Path

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def name_gen(count_strings: int, str_len_min: int, str_len_max: int, file_name):
    '''Записываем в файл случайные имена.'''

    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(count_strings):
            rand_string = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONSONANTS)
                                  for i in range(randint(str_len_min, str_len_max)))
            file.write(f'{rand_string.capitalize()}\n')


name_gen(8, 4, 7, 'Task02.txt')
