import random


class Board2048:
    def __init__(self, other_board=None):
        if not other_board:
            self.board = [[None] * 4 for _ in range(4)]
        else:
            self.board = [row[:] for row in other_board.board]

    def add_num(self):
        num = random.randint(1, 2) * 2
        empty_field = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] is None]
        if not empty_field:
            return False
        else:
            i, j = random.choice(empty_field)
            self.board[i][j] = num

    def left(self):
        new_board = [[None] * 4 for _ in range(4)]
        for r, row in enumerate(self.board):
            new_row = [x for x in row if x is not None]
            i = 0
            while i < len(new_row) - 1:
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row.pop(i + 1)
                i += 1
            for c, v in enumerate(new_row):
                new_board[r][c] = v
        if new_board == self.board:
            return False
        else:
            self.board = new_board
            return True

    def right(self):
        new_board = [[None] * 4 for _ in range(4)]
        for r, row in enumerate(self.board):
            new_row = [x for x in row[::-1] if x is not None]
            i = 0
            while i < len(new_row) - 1:
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row.pop(i + 1)
                i += 1
            for c, v in enumerate(new_row):
                new_board[r][3 - c] = v
        if new_board == self.board:
            return False
        else:
            self.board = new_board
            return True

    def up(self):
        self.transpose()
        result = self.left()
        self.transpose()
        return result

    def down(self):
        self.transpose()
        result = self.right()
        self.transpose()
        return result

    def transpose(self):
        self.board = list(map(list, zip(*self.board)))

    def pprint(self):
        for row in self.board:
            print('-'*21)
            row_str = ''
            for num in row:
                if num:
                    row_str += '|{:4d}'.format(num)
                else:
                    row_str += '|    '
            row_str += '|'
            print(row_str)

        print('-'*21)

    def max(self):
        return max(x for row in self.board for x in row if x is not None)

    def count(self):
        return sum(1 for row in self.board for x in row if x is not None)