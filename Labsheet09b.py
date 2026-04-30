#Problem Statement:Detect Suspicious Book Access Requests Using Linear Search
#Sample Input:8
#Sample Input: 1012 2050 3091 4120 1503 5220 6101 7099
#Sample Input:3091 3 
#Sample Output: Valid Access

n = int(input())
arr = list(map(int, input().split()))
x, k = map(int, input().split())

found = False

for i in range(n):
    if arr[i] == x:
        found = True
        if i < k:
            print("Valid Access")
        else:
            print("Late Access")
        break

if not found:
    print("Access ID Not Found")
