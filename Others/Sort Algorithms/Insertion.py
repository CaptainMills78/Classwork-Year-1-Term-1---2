def insertionSort(l, ascending=True):
    count_swaps = 0
    count_passes = 0
    for x in range(1, len(l)):
        count_passes += 1
        current = l[x]
        position = x
        while position > 0 and l[position - 1] > current:
            count_swaps += 1
            l[position] = l[position - 1]
            position = position - 1
        l[position] = current
    return l, count_swaps, count_passes


if __name__ == "__main__":
    import random
    import time
    List = []
    for x in range(10):
        List.append(random.randint(0, 100))
    start = time.time()
    l_sorted, swaps, passes = insertionSort(List, False)
    diff = time.time() - start
    print(l_sorted)
    print(swaps, "swaps")
    print(passes, "passes")
    print(diff, "time taken")