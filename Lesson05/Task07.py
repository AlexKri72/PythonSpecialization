# Создайте функцию-генератор.
# Функция генерирует N простых чисел,начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».

start_num = 2
quantity = 10


def isprime(n):
    '''Проверяем число на простоту.'''
    
    if n == start_num:
        return True
    for x in range(start_num, n):
        if n % x == 0:
            return False
        else:
            return True


def primes(n=start_num):
    '''Возвращаем простые числа'''

    while (True):
        if isprime(n): yield n
        n += 1


# Печатаем 10 простых чисел, начиная с 2
print(f'\n\n{quantity} простых чисел, начиная с 2: \n{"-" * 50}')
gen = primes()
for i in range(quantity):
    print(next(gen), end=' ')
print()
