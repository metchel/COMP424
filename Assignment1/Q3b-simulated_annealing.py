import math
import random
import time


def get_function(x):
    return math.sin(math.pow(x, 2)/2)/math.log((x+4), 2)


def step_random_solution(x):
    step_sizes = [0.1, 0.01, -0.1, -0.01]
    size = random.sample(step_sizes, 1)[0]
    x_new = x + size
    return x_new, get_function(x_new)


def valid(a):
    return 0 <= a <= 10


def evaluate_p(x_new, x, temp):
    prob = math.pow(math.e, -(get_function(x) - get_function(x_new))/temp)
    #print('probability of accepting ', get_function(x_new), 'over current y which is ', get_function(x), ' is ', prob)
    pseudo_boltzmann = [True]*(int(prob*10000)) + [False]*(int((1-prob)*10000))
    accept_value = random.choice(pseudo_boltzmann)
    return accept_value


def cool(temperature, alpha):
    return alpha*temperature


def run_simulated_annealing(x_start, t_start, alpha):
    t = t_start
    x_current = x_start
    x_max = x_current
    y_current = get_function(x_current)
    y_max = get_function(x_current)
    #print('x-start', x_start, 'y-start : ', y_max)
    steps = 0
    while t > 0.00001:
        #print('T = ', t)
        rand_x, rand_y = step_random_solution(x_current)
        if valid(rand_x):
            #print('x: ', rand_x, 'y: ', rand_y)
            if rand_y > y_max:
                x_current = rand_x
                y_current = rand_y
                y_max = rand_y
                x_max = x_current
                #print('new max')
            if rand_y > y_current:
                x_current = rand_x
                y_current = rand_y
                #print('greater')
            else:
                if evaluate_p(rand_x, x_current, t):
                    x_current = rand_x
                    y_current = rand_y
        steps = steps + 1
                    #print('less but accepted')
                #else:
                    #print('less, not accepted')
        #else:
            #print('invalid x: ', rand_x, 'out of range')
        t = cool(t, alpha)

    return x_max, y_max, steps


def main():
    starting_temps = [100000]
    cooling_factors = [0.999]
    starting_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for point in starting_points:
        for temp in starting_temps:
            for factor in cooling_factors:
                t0 = time.time()
                x, y, steps = run_simulated_annealing(point, temp, factor)
                te = time.time()
                diff = te - t0
                print(temp, ',', factor, ',', y, ',', diff, ',', steps, ',')

main()