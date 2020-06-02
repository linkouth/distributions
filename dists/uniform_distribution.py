import math

def get_distribution(m, a, b, x_arr):
    return [x for x in map(lambda x: a + x / m * b, x_arr)]


def handle(m, a, b, x_arr):
    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [math.floor(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        if x.is_integer():
            print(int(x))
        else:
            print(x)