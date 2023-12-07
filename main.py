from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    #implement Dijkstra's algorithm with added variable to keep track of edges visited
    def shortest_shortest_path_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            distance, edges, node = heappop(frontier)
            if node in visited:
                return shortest_shortest_path_helper(visited, frontier)
            else:
                visited[node] = distance, edges
                for neighbor, weight in graph[node]:
                    heappush(frontier, (distance + weight, edges + 1, neighbor)) #increase edges by 1 to show that 1 more edge has been visited 
                return shortest_shortest_path_helper(visited, frontier)
    frontier = []
    heappush(frontier,(0, 0, source)) #second variable in tuple keeps track of edges visited
    visited = dict()
    return shortest_shortest_path_helper(visited, frontier)

def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = dict() #create dictionary to store parent values
    parent[source] = None #source node has no parent
    nodes = deque() #queue of nodes
    nodes.append(source) #add source node to the queue
    while nodes: #while there are nodes remaining in the queue
        current = nodes.popleft() #current node is the leftmost node in queue (first loop is for source node)
        for neighbor in graph[current]: #find all neighbors of current node (for first loop all neighbors of the source node)
            if neighbor not in parent: #if the neighbor's parent has not already been identified, add it to the dictionary
                parent[neighbor] = current
                nodes.append(neighbor) #add neighbor to queue so its children can also be found  
    return parent
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = '' #string of characters 
    for node in parents:
        if parents[node] == None:
            source = node #if the node does not have a parent, it is the source node
    current_parent = parents[destination]
    if current_parent != source: #if the current parent is not the source, update the path  
        path = current_parent + path
    while current_parent != source: #continue updating parent until source node is reached
        current_parent = parents[current_parent]
        path = current_parent + path
    return path


graph = get_sample_graph()
parents = bfs_path(graph, 's')
print(get_path(parents, 'd'))