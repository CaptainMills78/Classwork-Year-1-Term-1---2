import nikalantha
import Wallis
import monte_carlo
import time
import math


def error_calc(PI):
    pi = float(math.pi)
    error = abs(pi-PI)
    error_percent = 100 * (error/pi)
    return error_percent


def main():
    num = int(input("Please enter the number of iterations/points to use in each method"))
    start1 = time.time()
    nikalan = nikalantha.nikalantha(num)
    end1 =time.time()
    diff1 = end1-start1
    print("Nikalantha Took", diff1, "seconds")
    start2 = time.time()
    wallis = Wallis.wallis(num)
    end2 = time.time()
    diff2 = end2-start2
    print("Wallis Took", diff2, "seconds")
    start3 = time.time()
    monte_c = monte_carlo.monteCarlo(num)
    end3 = time.time()
    diff3 = end3-start3
    print("Monte Carlo Took", diff3, "seconds")

    print("Nikalantha:")
    print("Pi value:", nikalan, "Error Percentage:", error_calc(nikalan))

    print("Wallis:")
    print("Pi value:", wallis, "Error Percentage:", error_calc(wallis))

    print("Monte Carlo:")
    print("Pi value:", monte_c, "Error Percentage:", error_calc(monte_c))


main()