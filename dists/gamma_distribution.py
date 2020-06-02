from math import log, cos, sin, sqrt, pi, floor, ceil, trunc

eps = 0.00001


def ln_of_arr(x_arr, m):
    acc = 1.0
    for x in x_arr:
        acc *= (1 - x / m)
    return log(acc)


def get_distribution(m, a, b, c, x_arr):
    result = []
    idx = 0
    if (c - trunc(c)) <= eps:
        c = int(c)
        while idx < len(x_arr) - c + 1:
            y = a - b * ln_of_arr(x_arr[idx : idx + c], m)
            result.append(y)
            idx += c
    else:
        k = int(c - 0.5)
        while idx < len(x_arr) - 2 * k - 1:
            z1 = (0 + 1 * sqrt(-2 * log(1 - x_arr[idx] / m)) * cos(2 * pi * x_arr[idx + 1] / m))
            z2 = (0 + 1 * sqrt(-2 * log(1 - x_arr[idx] / m)) * sin(2 * pi * x_arr[idx + 1] / m))
            y1 = a + b * (z1 * z1 / 2 - ln_of_arr(x_arr[idx + 2 : idx + k + 2], m))
            y2 = a + b * (z2 * z2 / 2 - ln_of_arr(x_arr[idx + k + 2 : idx + 2 * k + 2], m))
            result.append(y1)
            result.append(y2)
            idx += 2 * k + 2
    return result


def handle(m, a, b, c, x_arr):
    dist = get_distribution(m=m, a=a, b=b, c=c, x_arr=x_arr)
    list_to_print = [floor(x * 1000) / 1000 if x > 0 else ceil(x * 1000) / 1000 for x in dist]
    return list_to_print
