#Problem Statement:Manage Highest Bid Using a Priority Queue

import heapq

n = int(input())
bids = list(map(int, input().split()))

pq = []

# Push elements into max-heap (using negative values)
for b in bids:
    heapq.heappush(pq, -b)

# Get highest bid
highest = -heapq.heappop(pq)
print("Highest Bid:", highest)

# Get next highest bid (if exists)
if pq:
    print("Next Highest Bid:", -heapq.heappop(pq))