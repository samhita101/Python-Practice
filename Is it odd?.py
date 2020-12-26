# prompting user/ collecting input
print("Hello, to day we wll be finding out if your number is odd or even.")
print("Enter a number.")
number = int(input())


# defining function to check if number is odd or even
def is_odd():
    if number == 0:
        print("No 0's please.")
    if number % 2 == 0 and number != 0:
        print("Your number is even")
    else:
        if number % 2 == 1 and number != 0:
            print("Your number is odd.")


# calling the function
is_odd()