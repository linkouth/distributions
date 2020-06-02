from math import factorial, pow


def get_distribution(m, a, b, x_arr):
    result = []
    idx = 0
    while idx <= len(x_arr) - 1:
        x = x_arr[idx]
        u = x / m
        s = 0
        k = 0
        y = 0
        while k <= b - 1:
            s += factorial(b) / factorial(k) / factorial(b - k) * pow(a, k) * pow(1 - a, b - k)
            if s > u:
                y = k
                break
            k += 1
            y = b

        result.append(y)
        idx += 1
    return result


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [int(x) for x in dist]
    return list_to_print
