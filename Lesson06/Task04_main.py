from Task04 import puzzle

if __name__ == '__main__':
    count = puzzle("Какой последний день недели?", ["Воскресенье"], 4)
    print(['К сожалению Вы не угадали! ', f'Загадка отгадана с {count} попыток.'][count != 0])
