def insertionSort1(l):
    i = 1
    swaps = 0
    while i < len(l):
        j = i
        while j >0 and l[j-1] > l[j]:
            swaps += 1
            temp = l[j-1]
            l[j-1] = l[j]
            l[j] = temp
            j -= 1
        i += 1
    return l, i, swaps


def insertionSort2(l):
    for i in range(1, len(l)):
        swap = False
        item = l[i]
        j = i-1
        while j >= 0 and l[j] > item:
            swap = True
            l[j+1] = l[j]
            j -= 1
        if swap:
            l[j+1] = item
    return l


if __name__ == "__main__":
    import random
    import time
    List = []
    for x in range(10):
        List.append(random.randint(0, 100))
    print(List)
    start = time.time()
    l1_sorted, passes, swaps = insertionSort1(List)
    diff = time.time() - start
    print(l1_sorted)
    print(swaps, "swaps")
    print(passes, "passes")
    print(diff, "time taken")
    start = time.time()
    l2_sorted = insertionSort2(List)
    diff = time.time() - start
    print(l2_sorted)
