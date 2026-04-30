#Problem Statement: Probability of Drawing a Specific Card Combination
#Sample Input - 5 2 
#Sample Output - 0.274280

def combination(n, k):
    if k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result

k, r = map(int, input().split())

favorable = combination(13, r) * combination(39, k - r)
total = combination(52, k)

probability = favorable / total
print(f"{probability:.6f}")