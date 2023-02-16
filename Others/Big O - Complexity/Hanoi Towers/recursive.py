import timeit
import tracemalloc

import matplot_base

x = []
y1 = []
y2 = []


# Recursive Python function to solve tower of hanoi
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


for i in range(0, 18, 1):
    n = i
    x.append(n)
    tracemalloc.start()
    start = timeit.default_timer()
    TowerOfHanoi(n, 'A', 'C', 'B')
    y1.append((timeit.default_timer() - start) * 1000)
    current, peak = tracemalloc.get_traced_memory()
    y2.append(peak / 1000)
    tracemalloc.stop()

matplot_base.plotGraph(x, y1, "Number of Disks", "Time Taken", "Time complexity")
matplot_base.plotGraph(x, y2, "Number of Disks", "Memory Allocated", "Space complexity")
