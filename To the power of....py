# prompting the user/collecting the input

print("User we will be finding the power of a number.")
print("User give me a number:")
number = int(input())
print("User give me a number to multiply with the other as the exponent of ten.")
exponent = int(input())


# defining the function
def power():
    print(number * (10**exponent))


# calling the function
power()