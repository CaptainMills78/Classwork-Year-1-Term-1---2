def quickSort(l, start, end):
    if end-start == 1:
        return
    fixed = start
    movable = end
    while fixed != movable:
        if fixed > movable:
            if l[fixed] < l[movable]:
                temp = l[fixed]
                l[fixed] = l[movable]
                l[movable] = temp

                temp = fixed
                fixed = movable
                movable = temp
                movable -= 1
            else:
                movable += 1
        elif movable > fixed:
            if l[fixed] > l[movable]:
                temp = l[fixed]
                l[fixed] = l[movable]
                l[movable] = temp

                temp = fixed
                fixed = movable
                movable = temp
                movable += 1
            else:
                movable -= 1
    if fixed-1 >= 0:
        quickSort(l, start, fixed-1)
    if fixed+1 <= len(l)-1:
        quickSort(l, fixed+1, end)

    return l


if __name__ == "__main__":
    import random
    import time
    list2 = []
    length = int(input("Please enter the length of the list:"))
    for x in range(length):
        list2.append(random.randint(0, 1000))
    start_time = time.time()
    print(quickSort(list2, 0, len(list2)-1))
    diff = time.time() - start_time
    print("The sort took "+str(diff)+" seconds")