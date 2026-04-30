#Labsheet 30
#In a chess-like game with multiple pieces and obstacles, design an algorithm to determine the best move for a player.
#Using the Minimax algorithm with Alpha-Beta pruning to efficiently evaluate the game tree and choose the optimal move.
#Find the best possible move by exploring all possible game states and minimizing computation using pruning.


def minimax(depth, node, maximizing, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth+1, node*2+i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth+1, node*2+i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

depth = int(input())
values = list(map(int, input().split()))

print(minimax(0, 0, True, values, float('-inf'), float('inf'), depth))