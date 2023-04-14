# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
def trans_to_dict(**kwargs) -> dict:
    '''Переделываем принятые аргументы в словарь'''

    return {value if hashable_or_unhashable(value) else str(value): key for key, value in kwargs.items()}


def hashable_or_unhashable(obj):
    '''Проверяем на хэшируемость'''

    try:
        hash(obj)
        return True
    except Exception:
        return False


print(trans_to_dict(arg1='string', arg2=2023, arg3=False, arg4=10.2, arg5=['string', 1.38, 2],
                    arg6={1: '1', 2: '2'}))
