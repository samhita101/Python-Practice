# prompting the user and getting input
print("Today we will find out if the 2 numbers you input are equal.")
print("User give your first number.")
Number_one = float(input())
print("User give your second number.")
Number_two = float(input())


# defining the function that checks if they are equal

def equal():
    if Number_one == Number_two:
        print("Your numbers are equal.")
    else:
        print("Your numbers are not equal.")


# calling the function

equal()