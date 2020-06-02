from math import log, cos, sin, sqrt, pi, floor, ceil, exp


def get_distribution(m, a, b, x_arr):
    result = []
    idx = 0
    while idx <= len(x_arr) - 2:
        z1 = (0 + 1 * sqrt(-2 * log(1 - x_arr[idx] / m)) * cos(2 * pi * x_arr[idx + 1] / m))
        z2 = (0 + 1 * sqrt(-2 * log(1 - x_arr[idx] / m)) * sin(2 * pi * x_arr[idx + 1] / m))
        result.append(a + exp(b - z1))
        result.append(a + exp(b - z2))
        idx += 2
    return result


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [floor(x * 1000) / 1000 if x > 0 else ceil(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        print(x)
