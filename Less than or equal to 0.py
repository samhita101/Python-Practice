# prompting the user and collecting input
print("Give me a number I will try to find to find out if it is less than 0")
print("Give me a number:")
number = float(input())

# defining the function
def zero():
    if number < 0:
        print("your number is less than 0.")
    else:
        if number == 0:
            print("your number is equal of 0.")
        else:
            if number > 0:
                print("your number is greater than 0.")


# calling the function
zero()