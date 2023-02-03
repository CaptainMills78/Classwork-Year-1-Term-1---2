import random
import time


# Sub-routines


def monteCarlo(N):
    if __name__ != "__main__":
        r = 10
    else:
        r = int(input("Please enter the radius:"))
    nPoints = N
    circleCount = 0
    start = time.time()
    for x in range(0, nPoints):
        ran1 = random.randrange(-r, r)
        ran2 = random.randrange(-r, r)
        if (ran1 * ran1 + ran2 * ran2 <= (r**2)):
            circleCount = circleCount + 1
    PI = 4.0 * circleCount / nPoints
    end = time.time()
    difference = end - start
    if __name__ == "__main__":
        print("It took " + str(difference) + " seconds to complete this procedure.")
    return float(PI)


if __name__ == "__main__":
    print("Pi is " + float(monteCarlo(100)))
