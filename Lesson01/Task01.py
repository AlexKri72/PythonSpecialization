#   Программа загадывает число от 0 до 1000.
#   Необходимо угадать число за 10 попыток.
#   Программа должна подсказывать «больше» или «меньше» после каждой попытки.
#   Для генерации случайного числа используйте код:
#   from random import randint
#   num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
import os

os.system("cls")

attempts = 10
count = attempts + 1
left = 0
right = 1001
num = randint(left, right)

print(
    f'Я загадал число от 0 до 1000, а Вам нужно угадать его за 10 попыток! \nПо секрету - загадано число: {num} ')
while attempts > 0:
    try:
        answ = int(input(f'У Вас {attempts} попыток. Введите Ваш вариант ответа : '))
    except ValueError:
        print('Нужно ввести число!')
        continue

    if right < answ or answ < left:
        print(f'Неправильный ввод! Используйте диапазон чисел от {left} до {right}!')
        continue
    if answ < num:
        print(f'Загаданное число больше {answ}, попробуйте еще раз. ')
        attempts -= 1
        continue
    elif answ > num:
        print(f'Загаданное число меньше {answ}, попробуйте еще раз. ')
        attempts -= 1
        continue
    else:
        print("Ура! Число угадано с ", count - attempts, "попытки.")
        break
if attempts == 0: print('К сожалению Вы не смогли угадать число за 10 попыток! Может повезет в другой раз...')
