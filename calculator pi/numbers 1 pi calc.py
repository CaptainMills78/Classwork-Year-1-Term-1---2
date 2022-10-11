import random
import time
from decimal import *
#################Sub-routines#########


def monteCarlo():
    nPoints = int(input("How many points would you like to check?"))
    circleCount = 0
    start = time.time()
    for x in range(0,nPoints):
        ran1 = random.randrange(-10,10)
        ran2 = random.randrange(-10,10)
        if (ran1 * ran1 + ran2 * ran2 <= 100):
            circleCount = circleCount + 1
    PI = 4.0*circleCount/nPoints
    end = time.time()
    difference = end - start
    print("It took " + str(difference) + " seconds to complete this procedure.")
    return PI

def series():
    print("The series used will be the Nilakantha Series.")
    getcontext().prec = 100
    s = Decimal(1)
    PI = Decimal(3)
    n = int(input("How many iterations? (Longer is more accurate, but, well... longer!)"))
    start = time.time()
    for i in range(2, n * 2, 2):
        PI = PI + s * (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
        s = -1 * s
    end = time.time()
    diff = end-start
    print("It took " + str(diff) + " seconds to complete this procedure.")
    return PI

#Hello


#############################################Main Code###################################################


print("Welcome to the pi calculator with circles of radius 10!")
userIn = input("Would you like to perform the Monte Carlo method (mc), or the Series method (se)?").lower()


if userIn == "mc":
    print("Monte Carlo it is!")
    pi = monteCarlo()

elif userIn == "se":
    print("Series it is!")
    pi = series()
else:
    print("Not Valid")

print("Pi is "+str(pi)+" with the method you used.")