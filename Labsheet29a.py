#Fastest Path with Time Constraints
#Problem Statement: In a more complex treasure hunt, there are multiple paths connecting different locations. Each path has:

#A cost
#A time constraint

#To determine the fastest way to reach the treasure from a given starting point while considering both cost and time associated with each path.


import heapq

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, c, t = map(int, input().split())
    graph[u].append((v, c, t))

src, dest, maxTime = map(int, input().split())

pq = [(0, 0, src)]  # cost, time, node
visited = {}

while pq:
    cost, time, node = heapq.heappop(pq)

    if node == dest:
        print(cost)
        break

    for nei, c, t in graph[node]:
        newTime = time + t
        newCost = cost + c

        if newTime <= maxTime:
            heapq.heappush(pq, (newCost, newTime, nei))