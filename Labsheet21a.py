#Problem Statement:Design a File System Structure Using Trees and Hash Tables

from collections import defaultdict

n = int(input())

tree = defaultdict(list)
file_index = {}

# Input directory-file mapping
for _ in range(n):
    directory, file = input().split()
    tree[directory].append(file)
    file_index[file] = True

search_file = input()

# Print file system structure
print("File System Structure")
for directory in tree:
    print(directory, "->", *tree[directory])

# Search result
print("\nSearch Result")
if search_file in file_index:
    print("File Found")
else:
    print("File Not Found")