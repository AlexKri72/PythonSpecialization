# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

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
        safe_puzzle_result(key, count if count != 0 else 'Не угадано')

    print_result(_result_dict)


def puzzle(question: str, answers: list[str], count=3) -> int:
    '''Разгадыватель загадок'''

    other_count = 0
    while other_count < count:
        print(f'{question}. У Вас {count - other_count} попытки')
        other_count += 1
        if input('Ваш вариант: ').lower() in list(map(lambda x: x.lower(), answers)):
            return other_count
    return 0


_result_dict = {}


def safe_puzzle_result(puzzle: str, count: int):
    '''сохраняет результаты угадывания в защищенный словарь'''

    _result_dict[puzzle] = count


def print_result(my_dict: dict):
    print('-' * 100, '\nРезультаты угадывания: ')
    [print(*(key, val)) for key, val in my_dict.items()]
