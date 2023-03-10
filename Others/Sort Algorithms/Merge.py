def sort(l1, l2):
    p1 = 0
    p2 = 0
    result = []
    while p1 != len(l1) and p2 != len(l2):
        if l1[p1] < l2[p2]:
            result.append(l1[p1])
            p1 += 1
        else:
            result.append(l2[p2])
            p2 += 1
    if p1 != len(l1):
        for i in range(p1, len(l1)):
            result.append(l1[x])
    elif p2 != len(l2):
        for i in range(p2, len(l2)):
            result.append(l2[p2])
    return result


def split(l):
    low = 0
    high = len(l)-1
    if low < high:
        mid = (low+high)//2


if __name__ == "__main__":
    import random
    list1 = []
    list2 = []
    for x in range(10):
        list1.append(random.randint(0, 100))
        list2.append(random.randint(0, 100))
    list1.sort()
    list2.sort()
    print(list1)
    print(list2)
    print(sort(list1, list2))
