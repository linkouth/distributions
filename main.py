import argparse
from enum import Enum
from collections import namedtuple

from dists import uniform_distribution, logistic_distibution, binomial_distribution, lognorm_distribution, \
    normal_distribution, triangle_distribution, exponential_distribution, gamma_distribution, standard_distribution


class Dists(Enum):
    ST = 'st'
    UN = 'un'
    TR = 'tr'
    EX = 'ex'
    NR = 'nr'
    GM = 'gm'
    LN = 'ln'
    LS = 'ls'
    BI = 'bi'


def parse_data(args):
    if args.m is None:
        m = 10000
    else:
        m = int(args.m)

    x_arr = []
    if args.f is None:
        print('Press Enter if you want compute the distribution')
        print('Input the sequance: ')
        buffer_string = input().strip()
        while buffer_string != '':
            try:
                x_arr.append(int(buffer_string))
                buffer_string = input().strip()
            except Exception as e:
                break
    else:
        with open(args.f, 'r') as file:
            for line in file.readlines():
                x_arr.append(int(line.strip()))

    Data = namedtuple('Data', ['m', 'a', 'b', 'c', 'x_arr', 'o'])

    return Data(m=m, a=args.a, b=args.b, c=args.c, x_arr=x_arr, o=args.o)


def output_data(arr, path):
    if path is None:
        for a in arr:
            print(f"{a}")
    else:
        with open(path, 'w') as output:
            for a in arr:
                output.write(f'{a}\n')


def main():
    parser = argparse.ArgumentParser(description='Bringing the PRN sequence to the specified distribution')
    parser.add_argument('-f', help='Path to file with input sequance')
    parser.add_argument('-o', help='Path to output file')
    parser.add_argument('-d', type=str, help='Type of the specific distribution')
    parser.add_argument('-m', help='Parameter m')
    parser.add_argument('-a', help='Parameter a')
    parser.add_argument('-b', help='Parameter b')
    parser.add_argument('-c', help='Parameter c')

    args = parser.parse_args()
    dist_type = str(args.d).lower()

    input_data = parse_data(args)

    if dist_type == Dists.ST.value:
        dist = standard_distribution.handle(
            m=input_data.m,
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.UN.value:
        dist = uniform_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.TR.value:
        dist = triangle_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.EX.value:
        dist = exponential_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.NR.value:
        dist = normal_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.GM.value:
        dist = gamma_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=float(input_data.b),
            c=float(input_data.c),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.LN.value:
        dist = lognorm_distribution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.LS.value:
        dist = logistic_distibution.handle(
            m=input_data.m,
            a=int(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)
    elif dist_type == Dists.BI.value:
        dist = binomial_distribution.handle(
            m=input_data.m,
            a=float(input_data.a),
            b=int(input_data.b),
            x_arr=input_data.x_arr
        )
        output_data(dist, input_data.o)


if __name__ == '__main__':
    main()
