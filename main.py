import standard_distribution
import uniform_distribution
import triangle_distribution
import exponential_distribution
import normal_distribution
import lognorm_distribution
import logistic_distibution
import binomial_distribution
import gamma_distribution


def main():
    standard_distribution.handle_standard_distribution()
    uniform_distribution.handle_normal_distribution()
    triangle_distribution.handle()
    exponential_distribution.handle()
    normal_distribution.handle()
    lognorm_distribution.handle()
    logistic_distibution.handle()
    binomial_distribution.handle()
    gamma_distribution.handle()


if __name__ == '__main__':
    main()
