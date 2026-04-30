#Labsheet 22
#An online shopping cart can be represented as a tree, where each node represents an item or a category of items.
#Write an algorithm to calculate the total price of all items in the shopping cart.
#Tree traversal, calculating sums within a tree structure

def dfs(node, tree, price):
    total = price[node]
    for child in tree[node]:
        total += dfs(child, tree, price)
    return total

n = int(input())
tree = {}
price = {}
root = -1

for _ in range(n):
    node, parent, p = map(int, input().split())
    price[node] = p
    tree[node] = []
    if parent == -1:
        root = node
    else:
        tree.setdefault(parent, []).append(node)

print(dfs(root, tree, price))