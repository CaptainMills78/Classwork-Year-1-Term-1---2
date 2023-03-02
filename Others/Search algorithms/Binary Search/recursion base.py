def binarySearchRecursion(l, low, high, target):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if l[mid] == target:
            return True
        elif target < l[mid]:
            return binarySearchRecursion(l, low, mid - 1, target)
        else:
            return binarySearchRecursion(l, mid + 1, high, target)


if __name__ == "__main__":
    List = [3, 6, 7, 8, 99, 101]
    print(binarySearchRecursion(List, 0, len(List)-1, 7))
    print(binarySearchRecursion(List, 0, len(List)-1, 101))
    print(binarySearchRecursion(List, 0, len(List)-1, 3))
    print(binarySearchRecursion(List, 0, len(List)-1, 99))
    print(binarySearchRecursion(List, 0, len(List)-1, 1))