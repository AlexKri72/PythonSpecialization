# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

from Task06_1 import LevelException, AccessException


class User:
    MIN_LEVEL = 5
    MIN_ACCESS = 3

    def __init__(self, name, level, access):
        self.name = name
        if self.MIN_LEVEL <= level:
            self.level = level
        else:
            raise LevelException(level, self.MIN_LEVEL)
        if self.MIN_ACCESS <= access:
            self.access = access
        else:
            raise AccessException(access, self.MIN_ACCESS)


if __name__ == '__main__':
    u1 = User('Alex', 7, 7)
    # u2 = User('Alex', 2, 7)  # Task06_1.LevelException: Ошибка уровня  - 2, минимально необходимый уровень - 5
    # u3 = User('Alex', 7, 2)  # Task06_1.AccessException: Ошибка доступа - 2, минимальный доступ - 3
