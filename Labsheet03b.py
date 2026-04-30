#labsheet 03 - 3B
#Problem Statement: Modular Multiplication Checker
#Divisible
#Sample Input 1:
#100000 200000 1000000 4
#Sample Output 1:
#Divisible
#Sample Input 2:
#123456 789012 1000000 7
#Sample Output 2:
#Not Divisible

a, b, p, k = map(int, input("Enter the input values: ").split())


mod_prod = ((a % p) * (b % p)) % p


if mod_prod % k == 0:
    print("Divisible")
else:
    print("Not Divisible")