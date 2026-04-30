#Problem Statement: A treasure hunt involves a series of locations connected by different paths. Each path has an associated cost.

#A set of locations (nodes)
#A list of paths (edges) with their costs

#To determine the minimum cost required to reach the treasure from a given starting location.


import heapq

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

src, dest = map(int, input().split())

dist = {i: float('inf') for i in range(1, n + 1)}
dist[src] = 0

pq = [(0, src)]

while pq:
    d, node = heapq.heappop(pq)
    for nei, w in graph[node]:
        if d + w < dist[nei]:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

print(dist[dest])