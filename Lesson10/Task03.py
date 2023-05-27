# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
class Human:
    def __init__(self, name: str, patronimic: str, lastname: str, age: int, salary: int):
        self.name = name
        self.patrominic = patronimic
        self.lastname = lastname
        self.__age = age
        self.__salary = salary

    def full_name(self):
        return f'{self.name} {self.patrominic} {self.lastname}'

    def get_full_data(self):
        return f'{self.name} {self.patrominic} {self.lastname} age = {self.__age} salary = {self.__salary}'

    def birthday(self):
        self.__age += 1


if __name__ == '__main__':
    h1 = Human('Алексей', 'Валерьевич', 'Кривоногих', 51, 1200)
    print(h1.full_name())
    print(h1.get_full_data())
    h1.birthday()
    print(h1.get_full_data())
    # print(h1.age)  # AttributeError: 'Human' object has no attribute 'age' - недоступно для прямого обращения
    print(h1._Human__age)  # но есть возможность получить текущий возраст.
