import math

def get_distribution(m, a, b, x_arr):
    return [a - b * math.log(x / m) for x in x_arr]


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
    list_to_print = [math.floor(x * 1000) / 1000 for x in dist]
    for x in list_to_print:
        print(x)
