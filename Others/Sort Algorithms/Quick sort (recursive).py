def quickSort(l, start, end):
    if start >= end:
        return
    else:
        pivot = l[start]
        low = start+1
        high = end
        fin = False
        while not fin:
            while low <= high and l[low] <= pivot:
                low += 1
            while l[high] >= pivot and high >= low:
                high -= 1
            if low < high:
                temp = l[low]
                l[low] = l[high]
                l[high] = temp
            else:
                fin = True
        temp = l[start]
        l[start] = l[high]
        l[high] = temp

        quickSort(l, start, high-1)

        quickSort(l, high+1, end)

    return l


if __name__ == "__main__":
    import random
    import time
    list2 = []
    length = int(input("Please enter the length of the list:"))
    for x in range(length):
        list2.append(random.randint(0, 100000))
    start_time = time.time()
    print(quickSort(list2, 0, len(list2)-1))
    diff = time.time() - start_time
    print("The sort took "+str(diff)+" seconds")

