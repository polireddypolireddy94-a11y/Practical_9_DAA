
n = 4
graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

visited = [False] * n
visited[0] = True
cost = 0

for i in range(n - 1):
    minimum = 999
    x = y = -1

    for u in range(n):
        if visited[u]:
            for v in range(n):
                if not visited[v] and graph[u][v] != 0:
                    if graph[u][v] < minimum:
                        minimum = graph[u][v]
                        x, y = u, v

    print(x, "-", y, ":", minimum)
    cost += minimum
    visited[y] = True

print("Minimum Cost:", cost)
