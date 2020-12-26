# prompting user/collecting input for limit.
print("User, give me a positive integer, and I will find the number of multiples of three.")
print("Give me a number:")
number = int(input())


# finding # of #'s that are multiple of 3
multiples = number % 3
print((number - multiples)//3, "are the number of numbers that are multiples of 3.")