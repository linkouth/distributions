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


def handle():
    n = input().strip().split(' ')
    m, a, b = int(n[0][3:]), float(n[1][3:]), int(n[2][3:])
    x_arr = []
    buffer_string = input().strip()
    while buffer_string != '':
        try:
            x_arr.append(int(buffer_string))
            buffer_string = input().strip()
        except Exception as e:
            break

    dist = get_distribution(m=m, a=a, b=b, x_arr=x_arr)
    list_to_print = [int(x) for x in dist]
    for x in list_to_print:
        print(x)
