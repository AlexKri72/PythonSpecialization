# Возьмите задачу про банкомат из прошлых семинаров , которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.


class Bankomat:
    summa: float = 0
    percentage_for_withdrawal = 0.015  # 1.5 % за любую операцию
    multiplicity_of_the_operation = 50  # у.е. сумма операции должна быть кратна этой
    percentage_per_operation = 0.03  # 3 % - за каждую третью операцию
    min_percent = 30  # минимальная такса за операцию
    max_percent = 600  # максимальная такса за операцию
    max_sum = 5_000_000  # максимальная сумма капитала, после превышения коорой берется повышенный налог
    count = 0
    rich_tax = 0.1  # 10% -налог на операции для богатых

    def operation(operation_type: str):
        global summa
        while True:
            try:
                part = int(input('Введите сумму операции: '))
            except ValueError:
                print('Сумма введена некорректно!')
                continue
            if part % Bankomat.multiplicity_of_the_operation != 0:
                print('Сумма операции должна быть кратна 50 у.е.!')
                continue
            break

        if Bankomat.max_sum < summa:
            print('Применен налог на операции для богатых, удержано 10% от суммы операции - ', part * Bankomat.rich_tax,
                  'у.е.')
            summa -= part * Bankomat.rich_tax
            print('Сумма на счете составляет', summa, 'у.е.')

        match operation_type:
            case '1':
                summa += part
            case '2':
                if part > summa:
                    print('Сумма снятия превышает остаток!')
                    return
                print('Процент за снятие — 1.5 % от суммы снятия, но не менее 30 и не более 600 у.е.')
                percent = part * Bankomat.percentage_per_operation
                if Bankomat.max_percent < percent: percent = Bankomat.max_percent
                if percent < Bankomat.min_percent: percent = Bankomat.min_percent
                print('При выполнении операции удержано', percent, 'у.е')
                summa -= percent
                summa -= part
        Bankomat.count += 1
        if Bankomat.count % 3 == 0:
            print('Вам начислено ', Bankomat.percentage_per_operation * 100,
                  '% за третью операцию подряд! Сумма начисления составляет',
                  round(summa * Bankomat.percentage_per_operation, 2),
                  'у.е.')
            summa += summa * Bankomat.percentage_per_operation


if __name__ == '__main__':
    summa = Bankomat.summa
    while True:
        print('-' * 100)
        customer_choice = input(
            f"На счете сейчас {summa} у.е.\n1 - пополнить\n2 - снять\n3 - выйти\nВыберите тип операции: ")
        if customer_choice == '3':
            break
        elif customer_choice == '2' or customer_choice == '1':
            Bankomat.operation(customer_choice)
        else:
            continue
    print('\nДо новых встреч!')
