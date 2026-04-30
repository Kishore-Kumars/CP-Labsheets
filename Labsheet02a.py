#Sum of Large Numbers Modulo
#Enter n and m:  5 7 
#Enter array elements (numbers only):  10 20 30 40 50 
#Sample Output: Result: 3

n, m = map(int, input("Enter n and m: ").split())

arr = list(map(int,input("Enter array elements (numbers only): ").split()))

total = 0

for num in arr:
    total = (total + num) % m

print("Result:", total)
