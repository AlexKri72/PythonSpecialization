# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

summa = 0
percentage_for_withdrawal = 0.015  # 1.5 % за любую операцию
multiplicity_of_the_operation = 50  # у.е. сумма операции должна быть кратна этой
percentage_per_operation = 0.03  # 3 % - за каждую третью операцию
min_percent = 30  # минимальнуя такса за операцию
max_percent = 600  # максимальная такса за операцию
max_sum = 5_000_000  # максимальная сумма капитала, после превышения коорой берется повышенный налог
count = 0
rich_tax = 0.1  # 10% -налог на операции для богатых
safe_operation = []


def input_sum():
    '''модуль корректного ввода суммы операции'''

    while True:

        try:
            part = int(input('Введите сумму операции: '))
        except ValueError:
            print('Сумма введена некорректно!')
            continue
        if part % multiplicity_of_the_operation != 0:
            print('Сумма операции должна быть кратна 50 у.е.!')
            continue
        break
    return part


def Operation(operation_type):
    '''модуль проведения операции'''

    global summa
    global count
    global safe_operation

    part = input_sum()

    if max_sum < sum:
        print('Применен налог на операции для богатых, удержано 10% от суммы операции - ', part * rich_tax, 'у.е.')
        sum -= part * rich_tax
        safe_operation.append(part * rich_tax)
        print('Сумма на счете составляет', sum, 'у.е.')

    match operation_type:
        case '1':
            sum += part
            safe_operation.append(part)
        case '2':
            if part > sum:
                print('Сумма снятия превышает остаток!')
                return
            print('Процент за снятие — 1.5 % от суммы снятия, но не менее 30 и не более 600 у.е.')
            percent = part * percentage_per_operation
            if max_percent < percent: percent = max_percent
            if percent < min_percent: percent = min_percent
            print('При выполнении операции удержано', percent, 'у.е')
            sum -= percent
            safe_operation.append(-percent)
            sum -= part
            safe_operation.append(-part)
    count += 1
    if count % 3 == 0:
        print('Вам начислено ', percentage_per_operation * 100,
              '% за третью операцию подряд! Сумма начисления составляет', round(sum * percentage_per_operation, 2),
              'у.е.')
        sum += sum * percentage_per_operation
        safe_operation.append(sum * percentage_per_operation)


while True:
    print('-' * 100)
    customer_choice = input(
        f"На счете сейчас {summa} у.е.\n1 - пополнить\n2 - снять\n3 - выйти\nВыберите тип операции: ")
    if customer_choice == '3':
        break
    elif customer_choice == '2' or customer_choice == '1':
        Operation(customer_choice)
    else:
        continue
print('\nДо новых встреч!')
