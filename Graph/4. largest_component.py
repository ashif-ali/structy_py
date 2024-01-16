from collections import deque
def largest_component(graph):

    visited = set()
    max_maximum_size = 0
    
    def bfs(start, visited):
        queue = deque([start])
        visited.add(start)
        largeComponent = 0
        
        while queue:
            current_node = queue.pop()
            largeComponent += 1
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.appendleft(neighbor)
        return largeComponent
    
    for node in graph:
        if node not in visited:
            maximum_size = bfs(node, visited)
            max_maximum_size = max(max_maximum_size, maximum_size)
    return max_maximum_size
        
        

    



