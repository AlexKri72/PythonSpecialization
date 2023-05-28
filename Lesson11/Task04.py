# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """Создает единственный экземпляр класса, предыдущие экземпляры записывает в архив. """

    list_name = []
    list_age = []
    instance = None

    def __new__(cls, *args, **kwargs):
        """Сохраняет предыдущее значение экземпляра в массив."""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.list_name.append(cls.instance.name)
            cls.instance.list_age.append(cls.instance.age)
        return cls.instance

    def __init__(self, name, age):
        """Инициализация параметров."""
        self.name = name
        self.age = age

    def __str__(self):
        """Формирует вывод экземпляра для клиента."""
        return f'{self.name}, {self.age}, \
        archive names: {self.instance.list_name if self.instance.list_name else "Empty"}, \
        archive ages: {self.instance.list_age if self.instance.list_age else "Empty"}'

    def __repr__(self):
        """Формирует вывод экземпляра для программиста."""
        return f'Archive({self.name}, {self.age})'


if __name__ == '__main__':
    a1 = Archive('Alex', 51)
    print(a1)
    print(f'{a1= }')
    a2 = Archive('Irina', 43)
    print(a2)
    print(f'{a2= }')
    a3 = Archive('Olga', 27)
    print(a3)
    print(f'{a3= }')

    print('\nДокументация класса:\n', Archive.__doc__)
    help(Archive)
