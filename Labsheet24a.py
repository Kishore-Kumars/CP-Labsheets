#Problem Statement:Find the Minimum Moves for a Rook on a Chessboard

from collections import deque

n = int(input())

sr, sc = map(int, input().split())
tr, tc = map(int, input().split())

visited = [[False] * n for _ in range(n)]

queue = deque([(sr, sc, 0)])
visited[sr][sc] = True

while queue:
    r, c, moves = queue.popleft()

    if r == tr and c == tc:
        print(moves)
        break

    for i in range(n):
        # Move along row
        if not visited[r][i]:
            visited[r][i] = True
            queue.append((r, i, moves + 1))

        # Move along column
        if not visited[i][c]:
            visited[i][c] = True
            queue.append((i, c, moves + 1))