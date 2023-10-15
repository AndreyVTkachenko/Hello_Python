import random
import time
import os

SYMBOLS = "&%#$@*(@YyuUjJhHFfsqVNnv "
SYMBOLS_LEN = len(SYMBOLS)
PERIOD = 6
DELAY = 0.04


class ConsoleMatrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = self.create_matrix()

    def create_matrix(self):
        matrix = []
        for _ in range(self.height):
            row = []
            for position in range(self.width):
                if (position + 1) % 2 == 0:
                    row.append(' ')
                else:
                    row.append(random.choice(SYMBOLS))
            matrix.append(row)
        return matrix

    def show_matrix(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.matrix:
            print(''.join(row))

    def shift_matrix_elements(self, cycle):
        for w in range(0, self.width, 2):
            if w % PERIOD > cycle % PERIOD:
                continue
            for h in range(self.height - 1, -1, -1):
                if h == 0:
                    self.matrix[h][w] = random.choice(SYMBOLS)
                else:
                    self.matrix[h][w] = self.matrix[h - 1][w]


def main():
    width, height = os.get_terminal_size()
    console_matrix = ConsoleMatrix(width, height)

    cycle = 1
    while True:
        console_matrix.show_matrix()
        time.sleep(DELAY)
        console_matrix.shift_matrix_elements(cycle)
        cycle = (cycle + 1) % 1000


if __name__ == '__main__':
    main()
