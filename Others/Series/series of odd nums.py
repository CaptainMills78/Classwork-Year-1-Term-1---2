def series(N):
    y = 0
    for n in range(1, N+1):
        P = int(2*n - 1)
        y += P
    return(y)


num = int(input("Please enter the limit you want to reach:"))
print(series(num))
