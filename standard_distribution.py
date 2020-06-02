import math

def get_distribution(m, x_arr):
    return [x for x in map(lambda x: x / m, x_arr)]


def handle_standard_distribution():
    m = int(input().strip()[3:])
    x_arr = []
    buffer_string = input().strip()
    while buffer_string != '':
        x_arr.append(int(buffer_string))
        buffer_string = input().strip()

    dist = get_distribution(m=m, x_arr=x_arr)
    list_to_print = [math.floor(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        if math.fabs(x) < 0.00001:
            print(0)
        else:
            print(x)