def fib(num):
    n1 = 0
    n2 = 1
    n3 = 0
    if num == 0:
        fiba = 0
    elif num == 1:
        fiba = n2
    elif n > 0:
        for i in range(num-1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        fiba = n3
    return fiba


n = int(input("Please enter the item of the fibonacci sequence that you want to return:"))
f = fib(n)
print(f)
