# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

my_iter = iter({i: ord(i) for i in 'Напишите преобразование в одну строку'}.items())
[print(next(my_iter)) for _ in range(5)]