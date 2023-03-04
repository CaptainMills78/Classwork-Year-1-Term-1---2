def bubbleSort(l, ascending=True):
    sorted = False
    while not sorted:
        sorted = True
        for x in range(len(l)-1):
            if ascending:
                if l[x] > l[x+1]:
                    sorted = False
                    temp = l[x]
                    l[x] = l[x+1]
                    l[x+1] = temp
            else:
                if l[x] < l[x+1]:
                    sorted = False
                    temp = l[x]
                    l[x] = l[x + 1]
                    l[x + 1] = temp
    return l


if __name__ == "__main__":
    List = [4,8,4,2,3,5,1,9,8,4]
    print(bubbleSort(List))
