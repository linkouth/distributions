import math


def get_distribution(m, x_arr):
    return [x for x in map(lambda x: x / m, x_arr)]


def handle(m, x_arr):
    dist = get_distribution(m=m, x_arr=x_arr)
    list_to_print = [math.floor(x * 1000) / 1000 for x in dist]
    return [0 if math.fabs(x) < 0.00001 else x for x in list_to_print]
