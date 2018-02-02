class State:

    def __init__(self, l):
        self.board = l

    def get_board(self):
        return self.board

    def index2d(list2d, value):
        return next((i, j) for i, lst in enumerate(list2d)
                    for j, x in enumerate(lst) if x == value)

    def get_zero(self):
        return index2d(self.get_board(), 0)

    def get_board_ij(self, i, j):
        return self.board[i][j]

    def move(self, move):
        i, j = move
        x, y = self.get_zero()
        self.board[x][y] = self.board[i][j]
        self.board[i][j] = 0
        return self


init = State([[1, 4, 2], [5, 3, 0]])
goal = State([[0, 1, 2], [5, 4, 3]])


def index2d(list2d, value):
    return next((i, j) for i, lst in enumerate(list2d)
                for j, x in enumerate(lst) if x == value)


def get_next_states_moves(state):
    zero_x, zero_y = state.get_zero()
    moves = []
    states = []
    if zero_x+1 <= 1:
        moves.append((zero_x+1, zero_y))
        next_state = state.move(moves[0])
        states.append(next_state)
    if zero_y+1 <= 2:
        moves.append((zero_x, zero_y+1))
        next_state = state.move(moves[0])
        states.append(next_state)
    if zero_x-1 >= 0:
        moves.append((zero_x-1, zero_y))
        next_state = state.move(moves[0])
        states.append(next_state)
    if zero_y-1 >= 0:
        moves.append((zero_x, zero_y-1))
        next_state = state.move(moves[0])
        states.append(next_state)
    return states


def is_goal(state):
    return state.get_board()[0][0] == 0 and state.get_board()[0][1] == 1 and state.get_board()[0][2] == 2 and state.get_board()[1][0] == 5 and state.get_board()[1][1] == 4 and state.get_board()[1][2] == 3


def dfs(current_state):
    stack = list()
    visited = []
    visited.append(current_state)



dfs(init)