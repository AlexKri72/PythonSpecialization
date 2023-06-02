# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_dict_data(my_dict: dict, key: str, value=None):
    try:
        return my_dict[key]
    except KeyError:
        return value


if __name__ == '__main__':
    my_dict = {'один': 1, 'два': 2, 'три': 3}
    print(get_dict_data(my_dict, 'три'))
    print(get_dict_data(my_dict, 'четыре'))
