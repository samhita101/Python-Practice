# getting input and providing choices
print("Give me a number:")
num1 = float(input())
print("One more number:")
num2 = float(input())
print("Here are the operators you can choose from.\nEnter the operator of the choice.")
print("1. + \n2. - \n3. * \n4. /")
print("When entering your choice, only enter the operator and nothing else.")
operator = str(input())


# if invalid choices are inputted, print appropriate message
if num2 == 0 and operator == 4:
    print("Can't divide by 0!  Rerun program.")

if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Choice is invalid.  Rerun program.")


# defining function calculator which applies operator to numbers inputted
def calculator(arg, arg2):
    if operator == "+":
        print(arg + arg2, "is your result.")
    elif operator == "-":
        print(arg - arg2, "is your result.")
    elif operator == "*":
        print(arg * arg2, "is your result.")
    else:
        if operator == "/":
            print(arg / arg2, "is your result.")


# running function
calculator(num1, num2)
