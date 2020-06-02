import math


def get_distribution(m, a, b, x_arr):
    result = []
    idx = 0
    while idx <= len(x_arr) - 2:
        result.append(a + b * (x_arr[idx] / m + x_arr[idx + 1] / m - 1))
        idx += 2
    return result


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [math.ceil(x * 1000) / 1000 for x in dist]
    return list_to_print
