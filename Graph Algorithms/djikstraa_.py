import heapq
import timeit
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

example_graph = {
    'A': {'B': 10, 'D': 3},
    'B': {'A': 10, 'E': 6, 'C': 16},
    'C': {'B': 16, 'F': 8},
    'D': {'A': 3, 'E': 10},
    'E': {'B': 6, 'D': 10, 'F': 8},
    'F': {'C': 8, 'E': 8},
}

start_node = 'A'

start_time = timeit.timeit()
shortest_distances = dijkstra(example_graph, start_node)
end_time = timeit.timeit()

print(f"Shortest distances from node {start_node} to all other nodes:")
for node, distance in shortest_distances.items():
    print(f"Node {node}: {distance}")

runtime = end_time - start_time
print(f"Runtime: {runtime:.6f} seconds")