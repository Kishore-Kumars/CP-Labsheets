#Problem Statement:Implement Basic File System Operations (Create,Delete,Find)

from collections import defaultdict

tree = defaultdict(list)
file_index = {}

n = int(input())

for _ in range(n):
    parts = input().split()

    if parts[0] == "CREATE":
        parent, child = parts[1], parts[2]
        tree[parent].append(child)
        file_index[child] = True

    elif parts[0] == "DELETE":
        file = parts[1]
        file_index.pop(file, None)

    elif parts[0] == "FIND":
        file = parts[1]
        if file in file_index:
            print("File Found")
        else:
            print("File Not Found")