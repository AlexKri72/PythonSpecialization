from sys import argv
from Task03 import game

if __name__ == '__main__':
    game(*map(int, argv[1:]))
