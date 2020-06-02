import math

def get_distribution(m, a, b, x_arr):
    result = []
    idx = 0
    while idx <= len(x_arr) - 2:
        result.append(a + b * (x_arr[idx] / m + x_arr[idx + 1] / m - 1))
        idx += 2
    return result


def handle():
    m, a, b = [int(n[3:]) for n in input().strip().replace(': ', ':').split(' ')]
    x_arr = []
    buffer_string = input().strip()
    while buffer_string != '':
        try:
            x_arr.append(int(buffer_string))
            buffer_string = input().strip()
        except Exception as e:
            break

    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [math.ceil(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        print(x)
