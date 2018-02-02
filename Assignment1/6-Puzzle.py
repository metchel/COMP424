init_state = [[1,4,2], [5,3,0]]
goal_state = [[0,1,2], [5,4,3]]

def index2d(list2d, value):
    return next((i, j) for i, lst in enumerate(list2d)
                for j, x in enumerate(lst) if x == value)

def get_zero(state):
    return index2d(state, 0)

zero = get_zero(init_state)
print(zero)


