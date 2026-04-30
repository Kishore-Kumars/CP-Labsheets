#Problem Statement:Track the Highest Bid in a Single Auction

import heapq

n = int(input())
bids = list(map(int, input().split()))

pq = []

# Push elements into max-heap (using negative values)
for b in bids:
    heapq.heappush(pq, -b)

# Print highest bid
print(-pq[0])