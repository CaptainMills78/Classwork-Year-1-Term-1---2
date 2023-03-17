def quickSort(list, start, end):
    # This function is a quick sort algorithm
    # It takes a list as an argument and returns the list sorted
    # The algorithm is recursive
    # The algorithm is in-place
    # The algorithm is not stable
    # The algorithm is not adaptive
    # The algorithm is not optimized
    # The algorithm is not parallel
    if abs(end - start) == 1:
        return
    fixed = start
    movable = end
    while fixed != movable:
        if fixed > movable:
            if list[fixed] < list[movable]:
                temp = list[fixed]
                list[fixed] = list[movable]
                list[movable] = temp

                temp = fixed
                fixed = movable
                movable = temp
                movable -= 1
            else:
                movable += 1
        elif movable > fixed:
            if list[fixed] > list[movable]:
                temp = list[fixed]
                list[fixed] = list[movable]
                list[movable] = temp

                temp = fixed
                fixed = movable
                movable = temp
                movable += 1
            else:
                movable -= 1
    if fixed - 1 >= 0:
        quickSort(list, start, fixed - 1)
    if fixed + 1 <= len(list) - 1:
        quickSort(list, fixed + 1, end)
