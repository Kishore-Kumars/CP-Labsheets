#Problem Statement:String-Based Lookup Using Hash Tables
#Sample Input: 5
#Sample Input: apple 
#Sample Input: banana
#Sample Input: grape 
#Sample Input: orange 
#Sample Input: mango
#Sample Output:
#3
#Sample Input:apple 
#Found Sample Output
#Sample Input:pear 
#Not Found - Sample Output
#Sample Input:mango
#Found



n = int(input())
table = set()

for _ in range(n):
    table.add(input().strip())

q = int(input())

for _ in range(q):
    s = input().strip()

    if s in table:
        print("Found")
    else:
        print("Not Found")
