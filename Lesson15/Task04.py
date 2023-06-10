# Функция получает на вход текст вида:
#   “1-й четверг ноября”,
#   “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.


import logging
from _datetime import datetime,date

logging.basicConfig(
    filename='Task04.log',
    filemode='w',
    encoding='utf-8',
    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
    style='{',
    level=logging.INFO)
logger=logging.getLogger(__name__)

months = {'янв':1, 'фев':2, 'мар':3, "апр":4, "мая":5, "июн":6, "июл":7, "авг":8, "сен":9, "окт":10, "ноя":11, "дек":12}
weekdays = {"пон":1, "вто":2, "сре":3, "чет":4, "пят":5, "суб":6, "вос":7}


def text_to_date(text: str) :
    '''Переводим текст в дату.'''

    year = datetime.now().year              #  2023
    count, weekday, month = text.split()    #  3-я среда мая
    month = months[month[:3]]               #  5
    weekday = weekdays[weekday[:3]]-1       #  2
    count = int(count[0])                   #  3
    logger.info(f'{count} по счету ,  день недели {weekday}, месяц {month}, год {year}')
    count_week = 0
    for day in range(1, 31 + 1):
        result = date(year=year, month=month, day=day)
        if result.weekday() == weekday:
            count_week += 1
            if count_week == count:
                return result

if __name__=='__main__':
    print('1-й четверг ноября: ',text_to_date('1-й четверг ноября'))
    print('3-я среда мая: ',text_to_date('3-я среда мая'))
    print('4-й вторник мая: ',text_to_date('4-й вторник мая'))