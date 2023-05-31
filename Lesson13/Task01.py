# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения

def get_data():
    while True:
        try:
            a = input('Введите целое или вещественное число: ')
            a = int(a)
            break
        except:
            try:
                a = float(a)
                break
            except ValueError as e:
                print(f'Ошибка ввода данных {e}')
    return a


if __name__ == '__main__':
    print(get_data())
