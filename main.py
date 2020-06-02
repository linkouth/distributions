import argparse
from enum import Enum

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


def main():
    parser = argparse.ArgumentParser(description='Bringing the PRN sequence to the specified distribution')
    parser.add_argument('-f', help='Path to file with input sequance')
    parser.add_argument('-d', type=str, help='Type of the specific distribution')
    parser.add_argument('-m', help='Parameter m')
    parser.add_argument('-a', help='Parameter a')
    parser.add_argument('-b', help='Parameter b')


    args = parser.parse_args()
    dist_type = str(args.d).lower()

    if args.m is None:
        m = 10000
    else:
        m = int(args.m)

    if dist_type == Dists.ST.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            standard_distribution.handle(
                m=m,
                x_arr=x_arr
            )
    elif dist_type == Dists.UN.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            uniform_distribution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.TR.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            triangle_distribution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.EX.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            exponential_distribution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.NR.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            normal_distribution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.GM.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            gamma_distribution.handle(
                m=m,
                a=int(args.a),
                b=float(args.b),
                c=float(args.c),
                x_arr=x_arr
            )
    elif dist_type == Dists.LN.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            lognorm_distribution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.LS.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            logistic_distibution.handle(
                m=m,
                a=int(args.a),
                b=int(args.b),
                x_arr=x_arr
            )
    elif dist_type == Dists.BI.value:
        with open(args.f, 'r') as file:
            x_arr = [int(line.strip()) for line in file.readlines()]
            binomial_distribution.handle(
                m=m,
                a=float(args.a),
                b=int(args.b),
                x_arr=x_arr
            )


if __name__ == '__main__':
    main()
