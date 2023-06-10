# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое название дня недели и месяца, но и числовые, т.е не мая, а 5.

from Task04 import text_to_date
import  argparse
from datetime import datetime

if __name__=='__main__':
    weekdays={1:'вто',2:'сре',3:'чет',4:'пят',5:'суб',6:'вос',7:'пон'}
    months={1:'янв',2:'фев',3:'мар',4:'апр',5:'мая',6:'июн',7:'июл',8:'авг',9:'сен',10:'окт',11:'ноя',12:'дек'}

    parser= argparse.ArgumentParser(description='Получаем строку с датой')
    parser.add_argument('-count',type=str, default='1')
    parser.add_argument('-weekday',type=str, default=weekdays[datetime.now().weekday()])
    parser.add_argument('-month',type=str, default=months[datetime.now().month])

    args=parser.parse_args()

    weekday =  weekdays[int(args.weekday)]    if  args.weekday.isdigit()  else args.weekday
    month =  months[int(args.month)]    if  args.month.isdigit() else args.month

    print(f'{args.count} {weekday} {month} : ', text_to_date(f'{args.count} {weekday} {month}'))

    # python ./Lesson15/Task05.py -count='3-я' -weekday='среда'
