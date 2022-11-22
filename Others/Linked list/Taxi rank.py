head = 0
global head


def setRank():
    r = [["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66],
         ["", 66]]
    return r


def addTaxi(rank, reg, head1):
    pointer = head1
    while pointer >= 0:
        if rank[pointer][1] == 66:
            pointer = rank[pointer][1]
        else:
            rank[pointer][0] = reg
            rank[pointer][1] = pointer + 1
            pointer = -1
    return rank


def leavingTaxi(rank1, head):
    pointer1 = head
    while pointer1 >= 0:
        if rank1[pointer1][1] != 66:
            pointer1 = rank1[pointer1][1]
        else:
            temp = rank1[pointer1][1]
            rank1[pointer1][1] = 66
            if temp - 2 < 0:
                head = temp
            else:
                rank1[temp - 2][1] = temp
            pointer1 = -1
    return rank1


def main():
    taxi_rank = setRank()
    taxi_rank = addTaxi(taxi_rank, "RF23 TYZ", head)
    print(taxi_rank)
    taxi_rank = leavingTaxi(taxi_rank, head)
    print(taxi_rank)


main()
