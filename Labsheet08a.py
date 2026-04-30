#Problem Statement: Sort Student Marks Using Efficient Sorting (Merge Sort / Quick Sort)
#Sample Input:
#Enter the integer values for sample input: 6
#Enter the integer values for sample input2: 45 78 12 90 56 34 
#Expected Output: 12 34 45 56 78 90 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


n = int(input("Enter the integer values for sample input:"))
marks = list(map(int, input("Enter the integer values for sample input2:").split()))
sorted_marks = merge_sort(marks)

for x in sorted_marks:
    print(x, end=" ")