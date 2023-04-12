# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
#
#  *Верните все возможные варианты комплектации рюкзака.


dict = {
    'Фонарик': 0.5,
    'Палатка': 3,
    'Спички': 0.1,
    'Тушенка': 0.5,
    'Удочка': 1,
    'Спальник': 2,
    'Лопата': 2,
    'Котелок': 1,
    'Спиннинг': 0.7,
    'Наживка': 0.3,
}


def backpack(shop, max_weight):
    '''Считаем варианты комплектации рюкзака по заданной максимальной массе.'''

    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= max_weight:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result


print('Варианты комплектации рюкзака:')
for num, i in enumerate(backpack(dict, 6), start=1):
    print(num, i)
