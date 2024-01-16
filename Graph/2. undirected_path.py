from collections import deque

def undirected_path(edges, node_A, node_B):
    graph = {}
    visited = set()
    queue = deque([node_A])

    for edge in edges:
        first, second = edge
        graph.setdefault(first, set()).add(second)
        graph.setdefault(second, set()).add(first)

    while queue:
        current = queue.pop()
        for neighbour in graph.get(current, set()):
            if neighbour not in visited:
                visited.add(neighbour)
                if neighbour == node_B:
                    return True
                queue.appendleft(neighbour)

    return False
