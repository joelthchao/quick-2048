import pdb
from board import Board2048


class GameNode:
    def __init__(self, board):
        self.board = Board2048(board)
        self.children = []

    def score(self):
        own_score = naive_score(self.board)
        if len(self.children) == 0:
            return own_score
        else:
            return max(own_score, *[x.score() for x in self.children])


def search_game_play():
    # Init game play
    board = Board2048()
    board.add_num()
    board.add_num()
    board.pprint()

    root_node = GameNode(board)
    while True:
        root_node = search_best_step(root_node)
        if not root_node:
            break
        root_node.board.pprint()
        root_node.board.add_num()
        root_node.board.pprint()
        input()


def search_best_step(root_node, step=3):
    stack = [root_node]
    for _ in range(step):
        new_stack = []
        for game_node in stack:
            up_board = Board2048(game_node.board)
            res = up_board.up()
            if res:
                new_game_node = GameNode(up_board)
                game_node.children.append(new_game_node)
                new_stack.append(new_game_node)

            down_board = Board2048(game_node.board)
            res = down_board.down()
            if res:
                new_game_node = GameNode(down_board)
                game_node.children.append(new_game_node)
                new_stack.append(new_game_node)

            left_board = Board2048(game_node.board)
            res = left_board.left()
            if res:
                new_game_node = GameNode(left_board)
                game_node.children.append(new_game_node)
                new_stack.append(new_game_node)

            right_board = Board2048(game_node.board)
            res = right_board.right()
            if res:
                new_game_node = GameNode(right_board)
                game_node.children.append(new_game_node)
                new_stack.append(new_game_node)
        stack = new_stack

    best_child_board, best_score = None, -1
    for child_board in root_node.children:
        score = child_board.score()
        if score > best_score:
            best_child_board = child_board
            best_score = score
    return best_child_board


def naive_score(board):
    return board.max() - board.count()


if __name__ == '__main__':
    search_game_play()
