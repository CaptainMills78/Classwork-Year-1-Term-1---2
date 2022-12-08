
def main(start, end, graph, path=[]):
    path += [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = main(node, end, graph, path)
            if newpath == None:
                return newpath
            elif newpath[-1] == end:
                return newpath


if __name__ == "__main__":
    foodWeb = {'insect': ['grass'],
               'rabbit': ['grass'],
               'slug': ['grass'],
               'thrush': ['slug', 'insect'],
               'vole': ['insect'],
               'frog': ['insect'],
               'hawk': ['frog', 'vole', 'thrush'],
               'fox': ['rabbit', 'frog', 'vole']}
    to_print = main("vole", "thrush", foodWeb)
    print(to_print)
