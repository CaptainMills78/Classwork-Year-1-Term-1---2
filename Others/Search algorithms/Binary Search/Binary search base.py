
def binarySearch(l, target):
    mid = 0
    found = False
    first = 0
    last = len(l) - 1
    while first <= last and not found:
        mid = (first + last) // 2
        if l[mid] == target:
            found = True
        else:
            if target < l[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found, mid


if __name__ == "__main__":
    List = [1, 3, 4, 7, 12, 87]
    tar = int(input("Please enter something to search for"))
    f, pos = binarySearch(List, tar)
    if f:
        print("Found at "+str(pos))
    else:
        print("Not found")
