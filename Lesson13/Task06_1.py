class BaseException(Exception):
    pass


class LevelException(BaseException):
    def __init__(self, value, min_val):
        self.value = value
        self.min_val = min_val

    def __str__(self):
        return f'Ошибка уровня  - {self.value}, минимально необходимый уровень - {self.min_val}'


class AccessException(BaseException):
    def __init__(self, value, min_val):
        self.value = value
        self.min_val = min_val

    def __str__(self):
        return f'Ошибка доступа - {self.value}, минимальный доступ - {self.min_val}'
