# Доработаем задачи 3 и 4.
# Создайте класс проекта, который имеет следующие методы:
#   -загрузка данных (функция из задания 4)
#   -вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа.
# А если пользователь есть, получите его уровень из множества пользователей.
#   -добавление пользователя.
# Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json
from Task04 import User
from Task03 import LevelException, AccessException


class UserWorkShop:
    user_list = set()

    def __init__(self):
        UserWorkShop.load_users()
        pass

    @staticmethod
    def load_users(path: str = 'Task04.json'):
        with open(path, 'r', encoding='UTF-8') as file:
            user_dict = json.load(file)
        for level, user_list in user_dict.items():
            for uid, name in user_list.items():
                UserWorkShop.user_list.add(User(name, uid, level))

    def login(self, name: str, uid: str):
        login_user = User(name, uid)
        for user in UserWorkShop.user_list:
            if login_user == user:
                return user.level
        else:
            raise AccessException(name)

    def create(self, name: str, uid: str, level: str):
        cur_name, cur_uid = input('Введите имя и ID через пробел: ').split()
        if current_level := self.login(cur_name, cur_uid):
            if int(current_level) > int(level):
                return User(name, uid, level)
            else:
                raise LevelException(current_level, level)


baza = UserWorkShop()

print(baza.login('User_04', '456'))
print(baza.create('STONE', '17', '9'))
