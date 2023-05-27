# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from Task05 import Fish, Birds, Amphibians


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"fish": Fish, "birds": Birds, "amphibian": Amphibians}
        return types[animal_type.lower()]


if __name__ == '__main__':
    animal_from_fabric = AnimalFabric().make_animal("fish", "Стерлядь", 2, "серая")
    print(animal_from_fabric)
