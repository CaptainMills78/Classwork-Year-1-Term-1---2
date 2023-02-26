def linear(values, target):
    x = 0
    found = False
    position = -1
    while x < len(values) and not found:  # Need condition to finish once length has been reached to avoid
        # index-out-of-range error
        # Need not found condition unless duplication is possible - this will currently stop at finding one instance
        if values[x] == target: # If item found
            found = True
        else: # Increment
            x += 1
    if found:     # If item exists
        position = x     # Set position
    return found, position     # Return whether it has been found and the position as an optional result


if __name__ == "__main__":
    l = [1, 3, 7, 43, 12, 87, 4]
    linear(l, int(input("Please enter a target")))
