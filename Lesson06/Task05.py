# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ['puzzles']


def puzzles():
    '''Формирует загадки для разгадывателя'''

    puzzles_dict = {
        'Зимой и летом одним цветом - что это': ['ель', 'елка', 'ёлка', 'доллар'],
        ''' Полосатый и красивый,
Но не зебра, не енот.
Он съедобный, позитивный,
Сок и семена дает!''': ['арбуз', 'арбузик']
    }
    for key, val in puzzles_dict.items():
        count = puzzle(key, val)
        print(['К сожалению Вы не угадали! ', f'Загадка отгадана с {count} попыток.'][count != 0])


def puzzle(question: str, answers: list[str], count=3) -> int:
    '''Разгадыватель загадок'''

    other_count = 0
    while other_count < count:
        print(f'{question}. У Вас {count - other_count} попытки')
        other_count += 1
        if input('Ваш вариант: ').lower() in list(map(lambda x: x.lower(), answers)):
            return other_count
    return 0
