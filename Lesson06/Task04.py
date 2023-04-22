# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['puzzle']


def puzzle(question: str, answers: list[str], count=3) -> int:
    other_count = 0
    while other_count < count:
        print(f'{question}. У Вас {count - other_count} попытки')
        other_count += 1
        if input('Ваш вариант: ').lower() in list(map(lambda x: x.lower(), answers)):
            return other_count
    return 0
