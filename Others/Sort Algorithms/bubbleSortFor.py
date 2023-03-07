def bubbleAlternate(l, ascending=True):
    count_swaps = 0
    count_passes = 0
    for x in range(len(l) - 1):
        count_passes += 1
        for y in range(len(l) - 1 - x):
            if ascending:
                if l[y] > l[y+1]:
                    count_swaps += 1
                    temp = l[y]
                    l[y] = l[y+1]
                    l[y+1] = temp
            else:
                if l[y] < l[y+1]:
                    count_swaps += 1
                    temp = l[y]
                    l[y] = l[y+1]
                    l[y+1] = temp

    return l, count_swaps, count_passes


if __name__ == "__main__":
    import random
    List = []
    for x in range(10):
        List.append(random.randint(0, 100))
    print(List)
    l_sorted, swaps, passes = bubbleAlternate(List, False)
    print(l_sorted)
    print(swaps, "swaps")
    print(passes, "passes")
