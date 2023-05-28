# Создайте класс Моя Строка, где:
#       -будут доступны все возможности str
#       -дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyStr(str):
    """Сохраняет строку текста, автора и время создания строки."""

    def __new__(cls, text, name):
        """Добавляет к строке имя автора и время создания"""
        instance = super().__new__(cls, text)
        instance.name = name
        instance.time = time.time()
        return instance


if __name__ == '__main__':
    s1 = MyStr('Тварь я дрожащая или право имею?', 'Alex')
    print(s1, s1.name, s1.time)
