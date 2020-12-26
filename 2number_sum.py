def sum(arg1, arg2 ):
    total = arg1 + arg2
    print("Inside the function: ", total)
    return total
    print("Outside the function: ", total)


print("Input the first number")
input1 = int(input())
print("Input the second number")
input2 = int(input())

my_total = sum(input1,input2)
print(my_total, "is outside the function.")