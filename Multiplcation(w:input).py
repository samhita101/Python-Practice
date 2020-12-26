print("Today we will find the value of an exponent")


# defining function to find product
def power(ipt1, ipt2):
    total = ipt1 * ipt2
    return total


# getting values for parameters
print("User, give me a base value.")
product1 = float(input())
print("User give me an exponent value.")
product2 = float(input())

# calling function to find product
print(power(product1,product2), "is your answer.")