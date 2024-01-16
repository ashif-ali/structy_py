from collections import deque

def has_path(graph, src, dst):
  queue = deque([src])
  
  while len(queue) > 0:
    current = queue.popleft()
    for neighbor in graph[current]:
      if neighbor == dst:
        return True
      queue.appendleft(neighbor)
  return False
  