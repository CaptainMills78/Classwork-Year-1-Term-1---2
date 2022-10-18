import math


def calculateArcLength(l, h):
    radius = (h / 2) + ((l ** 2) / (8 * h))
    theta = 2 * math.asin(l / (2 * radius))
    aLength = 2 * math.pi * radius * (theta / (2 * math.pi))
    return aLength


def detail():
    length = int(input("Please enter the length of the bridge:"))
    height = (int(input("Please enter the height of the bridge (from deck level):")))
    print("The arc length is: " + str(calculateArcLength(length, height)))
    return


detail()
