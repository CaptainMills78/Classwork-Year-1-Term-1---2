def bubbleSort(l, ascending=True):
    sorted = False
    count_swaps = 0
    count_passes = 0
    while not sorted:
        count_passes += 1
        sorted = True
        for x in range(len(l)-1):
            if ascending:
                if l[x] > l[x+1]:
                    sorted = False
                    count_swaps += 1
                    temp = l[x]
                    l[x] = l[x+1]
                    l[x+1] = temp
            else:
                if l[x] < l[x+1]:
                    sorted = False
                    count_swaps += 1
                    temp = l[x]
                    l[x] = l[x + 1]
                    l[x + 1] = temp
    return l, count_swaps, count_passes


if __name__ == "__main__":
    import random
    List = []
    for x in range(0,10):
        List.append(random.randint(0, 100))
    print(List)
    l_sorted, swaps, passes = bubbleSort(List, False)
    print(l_sorted)
    print(swaps, "swaps")
    print(passes, "passes")
