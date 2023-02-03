import time
def nikalantha(N):
    y = float(3)
    x = float(0)
    count = 1
    for n in range(2, N*2, 2):
        P = ((-1)**(count+1))*(4/(n*(n+1)*(n+2)))
        x += P
        count += 1
    PI = y + x
    return float(PI)

if __name__ == "__main__":
    num = int(input("Please enter the limit you want to reach:"))
    start = time.time()
    print(nikalantha(num))
    end = time.time()
    diff = end-start
    print("This process took", diff, "seconds.")
