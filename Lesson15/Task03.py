# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
#   ○ уровень логирования,
#   ○ дату события,
#   ○ имя функции (не декоратора),
#   ○ аргументы вызова,
#   ○ результат.

import logging
import random
from functools import  wraps



logging.basicConfig(
    filename='Task03.log',
    filemode='w',
    encoding='utf-8',
    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
    style='{',
    level=logging.INFO)
logger=logging.getLogger(__name__)

def one(func):

    @wraps(func)
    def two(*args, **kwargs):
        result = func(*args)
        logger.info(f'Аргументы функции : {args}, результат : {result}')
        return result

    return two


@one
def three(a, b):
    return a + b


if __name__ == '__main__':
    print(three(random.randint(1, 11), random.randint(1, 11)))
