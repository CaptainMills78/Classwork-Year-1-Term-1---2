def find_path(graph, start, end, f_path=[]):
    if f_path is None:
        f_path = []
    f_path = f_path + [start]
    if start == end:
        return f_path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in f_path:
            f_newpath = find_path(graph, node, end, f_path)
            if f_newpath: return f_newpath
    return None


def find_all_paths(graph, start, end, f_a_path=[]):
    f_a_path = f_a_path + [start]
    if start == end:
        return [f_a_path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in f_a_path:
            newpaths = find_all_paths(graph, node, end, f_a_path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, shortestLength=-1, f_s_path=[]):
    f_s_path = f_s_path + [start]
    if start == end:
        return f_s_path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in f_s_path:
            if shortestLength == -1 or len(f_s_path) < (shortestLength - 1):
                newpath = find_shortest_path(graph, node, end, shortestLength, f_s_path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
                        shortestLength = len(newpath)
    return shortest
