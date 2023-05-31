# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
import os
from pprint import pprint


# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
class Valid:

    def __init__(self, name: str = None, lastname: str = None):
        self.name = name
        self.lastname = lastname

    def __set_name__(self, owner, name):
        self.param = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param, value)

    def validate(self, value: str):
        if not value.isalpha() or not value.istitle():
            raise ValueError(f'Bad data - {value}')


# Создайте класс студента.
class Student:
    name = Valid()
    lastname = Valid()

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.subject = {}
        self.tests = {}
        self.averadge_ball = {}

    # ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
    # ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    def __enter__(self):
        with open('Homework01.csv', 'r', newline='', encoding='utf-8') as f:
            read = csv.reader(f, delimiter=';')
            for row in list(read):
                sub, sub_num, sub_test = row
                self.subject[sub] = sub_num
                self.tests[sub] = sub_test

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    # ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

    @property
    def get_averadge_ball(self):
        for key, val in self.tests.items():
            summa = 0
            for i in val.split(','):
                summa += int(i)
            averadge = summa / len(val.split(','))
            self.averadge_ball[key] = round(averadge, 2)
        return self.averadge_ball

    @property
    def get_averadge_subjects(self):
        summa = 0
        count = 0
        for val in self.subject.values():
            for i in val.split(','):
                if i != '':
                    summa += int(i)
                    count += 1
        averadge = summa / count
        return averadge

    def __str__(self):
        return f'\nСтудент {self.name} {self.lastname}\n{"-" * 100}'


if __name__ == '__main__':
    s1 = Student('Alex', 'Kri')
    print(s1)
    with s1 as f:
        [print(key, ', оценки по предметам: ', val) for key, val in s1.subject.items()]
        print('-' * 100)
        [print(key, ', оценки по тестам: ', val) for key, val in s1.tests.items()]
    print('-' * 100, '\nСредний балл по тестам: \n')
    pprint(s1.get_averadge_ball)
    print('-' * 100, '\nСредний балл по оценкам: ', s1.get_averadge_subjects)
