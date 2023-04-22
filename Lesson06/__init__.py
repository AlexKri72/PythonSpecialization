# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
from Task02 import game
from Task03 import game
from Task04 import puzzle
from Task05 import puzzle, puzzles
from Task06 import puzzle, puzzles, safe_puzzle_result, print_result
from Task07 import calend, _leap_year

__all__ = ['game', 'puzzle', 'puzzles', 'safe_puzzle_result', 'print_result', 'calend', '_leap_year']
