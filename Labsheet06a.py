#Find the Unique Number(Using XOR)
#Sample Input - Enter number of elements:  5 
#Enter elements separated by space:  1 2 3 2 1 
#Sample Output - Enter number of elements:  5 
#XOR of all elements: 3

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements separated by space: ").split()))
ans = 0

for num in arr:
    ans ^= num

print("XOR of all elements:", ans)