#Problem Statement: Sort Race Results and Extract Top 10 Runners Using Efficient Sorting
#Sample Input:Enter the number of runners: 12 
#Enter the number of IDs: 120 101 
#Enter the number of IDs: 115 102 
#Enter the number of IDs: 130 103 
#Enter the number of IDs: 110 104 
#Enter the number of IDs: 118 105 
#Enter the number of IDs: 125 106
#Enter the number of IDs: 112 107 
#Enter the number of IDs: 119 108
#Enter the number of IDs: 117 109 
#Enter the number of IDs: 114 110 
#Enter the number of IDs: 116 111
#Enter the number of IDs: 113 112 
#Sample Output:
#101 120 
#112 107
#113 112
#114 110
#115 102
#116 111
#117 109
#118 105
#119 108
#120 101


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


n = int(input("Enter the number of runners:"))
runners = []

for _ in range(n):
    time, bib = map(int, input("Enter the number of IDs:").split())
    runners.append((time, bib))

sorted_runners = merge_sort(runners)

for i in range(min(10, len(sorted_runners))):
    print(sorted_runners[i][0], sorted_runners[i][1])
