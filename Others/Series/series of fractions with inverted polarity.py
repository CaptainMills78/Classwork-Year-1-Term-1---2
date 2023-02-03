def series(N):
    y = 0
    for n in range(1, N):
        P = 1/(2*n)
        y += P
    y += 1
    return(str(y))


num = int(input("Please enter the limit you want to reach:"))
print(series(num))