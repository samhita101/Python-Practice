# prompting user/collecting input for limit.
print("User, give me a number, and I will find the number of multiples of three.")
print("Give me a number:")
number = int(input())


# finding # of #'s that are multiple of 3, and subtracting them from variable number
multiples = number % 3
real_multiples = (number - multiples)//3
print(number - real_multiples, "are the number of numbers that aren't multiples of 3.")