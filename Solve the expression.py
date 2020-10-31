# function to take operator and and two numbers to calculate result
def expression_calculator(arg, arg2, arg3):
    if arg2 == "*":
        print(arg*arg3, "is your final result.")
    elif arg2 == "/":
        print(arg/arg3, "is your final result.")
    elif arg2 == "**":
        print(arg**arg3)
    elif arg2 == "+":
        print(arg+arg3, "is your final result.")
    else:
        if arg2 == "-":
            print(arg-arg3, "is your final result.")


# getting input for arguments
print("Give me the first number:")
num1 = float(input())
print("Give me the second number:")
num2 = float(input())
print("""The 5 possible operations are * for multiplication, / for division, + for addition, - for subtraction, 
and ** for powers.""")
print("Give me the sign.")
operator = str(input())

# division by 0 is undefined, so code for a "radha-proofer" for it
if num2 == 0 and operator == "/":
    print("Division by 0 is undefined.  Rerun program.")

# running the function
expression_calculator(num1, operator, num2)
