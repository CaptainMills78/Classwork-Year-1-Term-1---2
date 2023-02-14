import timeit
import tracemalloc
import matplot_base


# this function calculates the nth Fibonacci Number using iteration
def FibonacciItr(pos):
    counter = 0
    first = 0
    second = 1
    n = 0
    while counter <= pos:
        n = first + second
        first = second
        second = n
        counter = counter + 1
    return n


# this function calculates the nth Fibonacci Number using recursion

def FibonacciRec(pos):
    if pos <= 1:
        return 0
    if pos == 2:
        return 1
        # the function calls itself
    n = FibonacciRec(pos - 1) + FibonacciRec(pos - 2)
    return n


# here are two functions to measure time and memory


def memMesure(num):
    tracemalloc.start()
    # call Fibonacci Function either recrsive or iterative
    nth_fibo = FibonacciRec(num)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10 ** 3}KB; Peak was {peak / 10 ** 3}KB")
    tracemalloc.stop()
    return (peak / 10 ** 3)


def timeMeasure(num):
    start = timeit.default_timer()
    nth_fibo = FibonacciRec(num)
    end = timeit.default_timer()
    t = (
                end - start) * 1000000  # time in microseconds. To convert it milliseconds multiply times 1000, and for second multiply by 1
    print("Time of execution is " + str(t) + " microseconds")
    return t





x = []
y1 = []
y2 = []
print("This program calculates the nth Faibonacci number and prints time it takes and memory used")
number_start = 5
number_inc = 5
for number in range(number_start, 30, number_inc):
    x.append(number)
    y1.append(memMesure(number))
    y2.append(timeMeasure(number))
    number_inc *= 2
print(x)
print(y1)
print(y2)
matplot_base.plotGraph(x, y1, "Number", "Space (KB)", "Space Complexity")
matplot_base.plotGraph(x, y2, "Number", "Time (Microseconds)", "Time Complexity")


