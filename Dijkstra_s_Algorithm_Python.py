import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex) tuples
    priority_queue = [(0, start)]
    # Dictionary to store the shortest distance to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    # The distance to the start vertex is 0
    distances[start] = 0
    # Dictionary to store the path
    previous_vertices = {vertex: None for vertex in graph}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If a shorter path to current_vertex has been found, skip this one
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end
    
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    
    path = path[::-1]
    if path[0] == start:
        return path
    else:
        return []

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
end = 'D'
print("Shortest path from {} to {} is:".format(start, end), shortest_path(graph, start, end))

