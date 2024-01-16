# def connected_components_count(graph):
#     def dfs(node, visited):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs(neighbor, visited)

#     visited_nodes = set()
#     components_count = 0

#     for node in graph:
#         if node not in visited_nodes:
#             components_count += 1
#             dfs(node, visited_nodes)

#     return components_count
from collections import deque
def connected_components_count(graph):
  
  visited = set()
  count = 0
  

  def bfs(start, visited):
    queue = deque([start])
    visited.add(start)
    
    while queue:
      current_node = queue.pop()
      for neighbor in graph[current_node]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.appendleft(neighbor)
      
      

  for node in graph:
    if node not in visited:
      count += 1
      bfs(node, visited)
  return count













