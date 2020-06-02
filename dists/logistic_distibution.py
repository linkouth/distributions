from math import log, floor, ceil


def get_distribution(m, a, b, x_arr):
    result = []
    idx = 0
    while idx <= len(x_arr) - 1:
        x = x_arr[idx]
        u = x / m
        result.append(a + b * log(u / (1 - u)))
        idx += 1
    return result


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [floor(x * 1000) / 1000 if x > 0 else ceil(x * 1000) / 1000 for x in dist]
    return list_to_print
