def fact_find(n):
    total = 1
    if n == 0:
        total = 1
    else:
        for x in range(n, 1, -1):
            total = total * x
    return total


print(fact_find(0))
