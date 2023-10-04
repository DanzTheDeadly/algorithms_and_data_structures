from queue import SimpleQueue


def topological_sort(graph: list[list[int]]) -> list:
    in_degree = [0]*len(graph)
    for node in range(len(graph)):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    stack = [idx for idx in range(len(in_degree)) if in_degree[idx] == 0]
    res = []
    while stack:
        idx = stack.pop()
        res.append(idx)
        for neighbor_idx in graph[idx]:
            in_degree[neighbor_idx] -= 1
            if in_degree[neighbor_idx] == 0:
                stack.append(neighbor_idx)
    return res


def shortestPath(graph: list[list], start: int, end: int):
    shortest = [9999] * len(graph)
    shortest[start] = 0
    prev = [None] * len(graph)
    sorted_graph = topological_sort(graph)
    for idx in sorted_graph:
        for neighbor in graph[idx]:
            if shortest[idx] + 1 < shortest[neighbor]:
                shortest[neighbor] = shortest[idx] + 1
                prev[neighbor] = idx
    if not prev[end]:
        return False
    counter = shortest[end]
    res = [None] * (counter + 1)
    while counter >= 0:
        res[counter] = end
        end = prev[end]
        counter -= 1
    return res


def shortestPathBFS(graph: list[list[int]], start: int, end: int):
    shortest = [9999] * len(graph)
    shortest[start] = 0
    prev = [None] * len(graph)
    visited = [0] * len(graph)
    q = SimpleQueue()
    q.put(start)
    while not q.empty():
        node = q.get()
        if node != end:
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    shortest[neighbor] = shortest[node] + 1
                    prev[neighbor] = node
                    q.put(neighbor)
                    visited[neighbor] = 1
        else:
            counter = shortest[end]
            res = [None] * (counter + 1)
            while counter >= 0:
                res[counter] = end
                end = prev[end]
                counter -= 1
            return res
    return False