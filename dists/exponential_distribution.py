import math


def get_distribution(m, a, b, x_arr):
    return [a - b * math.log(x / m) for x in x_arr]


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [math.floor(x * 1000) / 1000 for x in dist]
    return list_to_print
