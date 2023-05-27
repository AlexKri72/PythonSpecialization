# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию, специфичную для данного класса.


# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):
    def __init__(self, color, *args):
        self.__color = color
        super().__init__(*args)

    def get_specific(self):
        return self.__color


class Birds(Animal):
    def __init__(self, feathers, *args):
        self.__feather = feathers
        super().__init__(*args)

    def get_specific(self):
        return self.__feather


class Amphibians(Animal):
    def __init__(self, number_of_limbs, *args):
        self.__number_of_limbs = number_of_limbs
        super().__init__(*args)

    def get_specific(self):
        return self.__number_of_limbs


if __name__ == '__main__':
    fish = Fish('красный', 'Форель', 3)
    bird = Birds('длинные и серые', 'Птичка', 6)
    amphibian = Amphibians(4, 'Крот', 12)
    print(f'Я рыба {fish.name}, мне {fish.age} лет , и у мой цвет {fish.get_specific()}')
    print(f'Я птица {bird.name}, мне {bird.age} лет , и мои перья {bird.get_specific()}')
    print(f'Я земноводное {amphibian.name}, мне {amphibian.age} лет , и у меня {amphibian.get_specific()} конечности')
