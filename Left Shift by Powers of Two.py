# defining function that calculates end result using two inputs
def shift_to_left(arg, arg2):
    power = arg2**2 # calculating second factor
    print(arg, ",", arg2, ",", arg*power)


# getting input for arg, arg2
print("give me your first number")
num1 = int(input())
print("give me the second number")
num2 = int(input())

# running function on num1, num2
shift_to_left(num1, num2)