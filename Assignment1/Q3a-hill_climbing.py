import math


# hill climbing for function y = (x^2/2)/(log2(x+4))
def get_function(x):
    return math.sin(math.pow(x, 2)/2)/math.log((x+4), 2)


def get_next_step(step_size, x_current):
    current_max = get_function(x_current)
    if x_current + step_size <= 10:
        x_left = x_current - step_size
    else:
        x_left = x_current
    if x_current - step_size >= 0:
        x_right = x_current + step_size
    else:
        x_right = x_current
    max_left = get_function(x_left)
    max_right = get_function(x_right)

    local_max = max(current_max, max_left, max_right)

    if local_max == max_left:
        return x_left
    if local_max == max_right:
        return x_right
    else:
        return 'LOCAL OPTIMUM REACHED'


def run_hill_climbing(x_start, step_size):
    max_y = get_function(x_start)
    steps = 0

    while get_next_step(step_size, x_start) != 'LOCAL OPTIMUM REACHED':
        steps = steps + 1
        x_start = get_next_step(step_size, x_start)
        max_y = get_function(x_start)

    return x_start, max_y, steps


def main():
    step_sizes = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    start_xs = [10]

    for size in step_sizes:
        for x in start_xs:
            #print(size)
            #print(x, ',', get_function(x))
            max_x, max_y, steps = run_hill_climbing(x, size)
            print(x, size, max_y)
            #print(steps)

main()

