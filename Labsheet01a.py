#Problem Statement: Tiered Discount Calculator
#Sample Input: 5533
#Sample Output: 4426

amount = int(input("Enter total purchase amount: "))
if amount < 1000:
 final_amount = amount
elif amount < 5000:
 final_amount = amount - (amount * 0.10)
elif amount < 10000:
 final_amount = amount - (amount * 0.20)
else:
 final_amount = amount - (amount * 0.25) - 500
print("Final amount to be paid:", int(final_amount))