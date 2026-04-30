#Problem Statement: Third-Place Finisher Using Basic Sorting
#Sample Input:Enter number of elements:  5 
#Sample Input: Enter the values:  12 15 10 18 14 
#Sample Output:Element at index 2 is: 14


n = int(input("Enter number of elements: "))
times = list(map(int, input("Enter the values: ").split()))

for i in range(1, n):
    key = times[i]
    j = i - 1

    while j >= 0 and times[j] > key:
        times[j + 1] = times[j]
        j -= 1

    times[j + 1] = key


print("Element at index 2 is:", times[2])