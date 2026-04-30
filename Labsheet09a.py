#Problem Statement:Search an Element using Linear Search
#Sample Input: Enter the input values: 6
#Enter the input values: 15 22 30 45 10 18 
#45
#3 

#Input
n = int(input("Enter the input values: "))
arr = list(map(int, input().split()))
x = int(input())

# Search
found = False

for i in range(n):
    if arr[i] == x:
        print(i)
        found = True
        break

# Output if not found
if not found:
    print("Not Found")