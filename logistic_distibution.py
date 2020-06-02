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

def handle():
    m, a, b = [int(n[3:]) for n in input().strip().split(' ')]
    x_arr = []
    buffer_string = input().strip()
    while buffer_string != '':
        try:
            x_arr.append(int(buffer_string))
            buffer_string = input().strip()
        except Exception as e:
            break

    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [floor(x * 1000) / 1000 if x > 0 else ceil(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        print(x)
