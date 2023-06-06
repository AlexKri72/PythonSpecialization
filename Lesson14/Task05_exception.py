class UserException(Exception):
    pass


class UserTypeStrError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение {self.value} должно быть числом!'


class UserValueError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение {self.value} должно быть больше нуля!'
