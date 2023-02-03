def series(N):
    y = 1
    for n in range(1, N+1):
        P = 1/(2*n)
        y *= P
    return(str(y))


num = int(input("Please enter the limit you want to reach:"))
print(series(num))