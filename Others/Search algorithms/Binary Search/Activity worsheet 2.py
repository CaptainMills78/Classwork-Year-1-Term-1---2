def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while low <= high:
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid
    return -1


a = [2, 4, 7, 8, 12, 88, 99, 101]
target = 7
assert binary_search(a, 1134) == -1, "value 1134 isn't in array but says it is"
assert binary_search(a, 2) == 0, "value 2 is in the zero element of array.begenning"
assert binary_search(a, 101) == 7, "value 101 is in the 7th element of array. end"
assert binary_search(a, 12) == 4, "value 12 is in the 4th element of array. midpoint"
