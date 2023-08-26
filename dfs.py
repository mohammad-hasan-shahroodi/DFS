def get_neighbors(current_vertex, graph):
    neighbors = []

    row = graph[current_vertex]
    for i in range(len(row)):
            number = row[i]
            if number != 0:
                neighbors.append(i)

    return neighbors

def dfs(visited, current_vertex, graph):
    if current_vertex in visited:
            return

    visited.append(current_vertex)
    neighbors = get_neighbors(current_vertex, graph)

    for neighbor in neighbors:
            dfs(visited, neighbor, graph)


graph = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
]
current_vertex = 0
dfs([], current_vertex, graph)