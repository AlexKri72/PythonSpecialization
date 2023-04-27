# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел.
# В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя, записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя, прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def mult_file(name_num_file, name_str_file, name_result_file):
    '''Собираем из двух файлов третий.'''

    with (
        open(name_str_file, 'r', encoding='UTF-8') as f_str,
        open(name_num_file, 'r', encoding='UTF-8') as f_num,
        open(name_result_file, 'w', encoding='UTF-8') as f_result
    ):
        names = f_str.readlines()
        numbers = f_num.readlines()
        for i in range(max(len(names), len(numbers))):
            a, b = numbers[i % len(numbers)].rstrip('\n').split('|')
            mult = float(a) * float(b)
            if 0 < mult:
                f_result.write(f'{names[i % len(names)].rstrip().upper()} {int(mult)}\n')
            else:
                f_result.write(f'{names[i % len(names)].rstrip().lower()} {abs(mult)}\n')


mult_file('Task01.txt', 'Task02.txt', 'Task03.txt')
