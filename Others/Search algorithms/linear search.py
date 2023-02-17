def linear(values, target):
    x = 0
    found = False
    while x < len(values) and not found:  # Need condition to finish once length has been reached to avoid
        # index-out-of-range error
        # Need not found condition unless duplication is possible - this will currently stop at finding one instance
        if values[x] == target:
            found = True
        else:
            x += 1
    print("In List? - " + str(found))
    if found:
        print("Target at position: " + str(x))


if __name__ == "__main__":
    l = [1, 3, 7, 43, 12, 87, 4]
    linear(l, int(input("Please enter a target")))
