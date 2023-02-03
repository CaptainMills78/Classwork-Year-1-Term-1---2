import time
def wallis(N):
    y = 1
    top = 0
    bottom = 1
    for n in range(1, N+1):
        if n % 2 == 1:
            top += 2
        else:
            bottom += 2
        P = top/bottom
        y *= P
    return(float(y*2))


if __name__ == "__main__":
    num = int(input("Please enter the limit you want to reach:"))
    start = time.time()
    print(wallis(num))
    end = time.time()
    diff = end-start
    print("This process took", diff, "seconds.")