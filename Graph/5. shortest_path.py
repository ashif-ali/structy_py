from collections import deque
def create_graph(edges):
    adlist = {}
    for edge in edges:
        first, second = edge
        adlist.setdefault(first, set()).add(second)
        adlist.setdefault(second, set()).add(first)
    return adlist


def shortest_path(edges, node_A, node_B):
    visited = set()
    graph = create_graph(edges)
    queue = deque([(node_A, 0)])
    
    while queue:
        current_node, distane = queue.popleft()
        
        if current_node == node_B:
            return distane
        
        for neighbour in graph.get(current_node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distane + 1))
    return -1
    
            
    