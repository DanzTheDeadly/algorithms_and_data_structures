def topological_sort(graph: list[list[int]]) -> list:
    in_degree = [0]*len(graph) # 
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
