def fact_find(n):
    total = 1
    if n == 0:
        return 1
    else:
        return n * fact_find(n-1)


print(fact_find(0))