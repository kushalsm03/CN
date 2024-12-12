def bellman_ford(vertices, edges, source):
    distance = [float('inf')] * vertices
    distance[source] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            print("Negative weight cycle detected")
            return

    print("Vertex Distance from Source")
    for i in range(vertices):
        print(f"{i}\t\t{distance[i]}")

# Example graph as a list of edges (u, v, weight)
edges = [
    (0, 1, 5), (0, 2, 7), (1, 2, 3),
    (1, 3, 4), (1, 4, 6), (3, 4, -1),
    (3, 5, 2), (4, 5, -3)
]
vertices = 6
source = 0
bellman_ford(vertices, edges, source)