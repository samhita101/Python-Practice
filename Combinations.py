import math
print("Today we are will find the number of combinations possible from from a number n and r.")
print("You will get to pick what n and r are equal to.")
print("Make sure you only enter POSITIVE INTEGERS as your numbers.")
print("Enter what you want n to be equal to: ")
n = int(input())
print("Now enter a value for r. Make sure it is LESS THAN your number for n.")
r = int(input())

if n <= r:
    print("Give a value for n that is greater than r.")
if n < 1 or r < 1:
    print("Give me positive numbers only.")

def combinations():
     print((math.factorial(n)/(math.factorial(r)*(math.factorial(n-r)))))

combinations()























