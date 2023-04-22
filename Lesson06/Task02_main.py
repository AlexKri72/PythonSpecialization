from Task02 import game

if __name__ == '__main__':
    min_limit = 1
    max_limit = 1000
    count_limit = 8
    print(f'Угадайте число в диапазоне от {min_limit} до {max_limit}.')
    game(min_limit, max_limit, count_limit)
