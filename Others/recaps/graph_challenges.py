graph = {
    "A":{"B":8, "C":5},
    "B":{"A":6, "D":1},
    "C":{"A":12, "D":6, "E":9},
    "D":{"C":6, "B":3, "E":2},
    "E":{"C":9, "D":2}
}

currentNode = input("Enter the node you want to check:")
print(graph[currentNode])

neighbour = input("Enter the edge you would like to check the cost of:")
print(graph[currentNode][neighbour])

def challenge2(g):
    target = "D"
    path = "C"
    head = "A"
    cost = 0
    for x in g[head]:
        if x == target:
            cost += g[head][target]