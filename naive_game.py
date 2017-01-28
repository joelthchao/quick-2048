from board import Board2048


def naive_game_play():
    # Init game play
    board = Board2048()
    board.add_num()
    board.add_num()
    board.pprint()

    while True:
        alive, board = naive_game_step(board)
        if not alive:
            break
        board.pprint()
        board.add_num()
        board.pprint()
        input()


def naive_game_step(board):
    valid_next_board = []

    up_board = Board2048(board)
    res = up_board.up()
    if res:
        valid_next_board.append(up_board)

    down_board = Board2048(board)
    res = down_board.down()
    if res:
        valid_next_board.append(down_board)

    left_board = Board2048(board)
    res = left_board.left()
    if res:
        valid_next_board.append(left_board)

    right_board = Board2048(board)
    res = right_board.right()
    if res:
        valid_next_board.append(right_board)

    if not valid_next_board:
        return False, None
    else:
        next_board = max(valid_next_board, key=lambda x: naive_score(x))
        return True, next_board


def naive_score(board):
    return board.max() - board.count()


if __name__ == '__main__':
    naive_game_play()
