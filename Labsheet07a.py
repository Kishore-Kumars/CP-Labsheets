#Problem Statement: Store Finishing Times in an Array/list
#Sample Input - Enter the number of values:  5 
#Sample Input - 12 15 10 18 14 
#Sample Output - 12 15 10 18 14 

n = int(input("Enter the number of values: "))
times = list(map(int, input("Enter the values: ").split()))

for t in times:
    print(t, end=" ")