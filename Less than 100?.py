# prompting user/collecting input
print('Today I will be taking the sum of 2 numbers and trying to find if the sum is < 100.')
print("User give your 1st number:")
first_num = float(input())
print("User give your 2st number:")
second_num = float(input())


# making the function that determines if the sum of the inputs is less than or greater than 100.

def theSum():
    total = first_num + second_num
    if total < 100:
        print("The sum is less than 100.")
    else:
        print("The sum is not less than 100.")


# calling the function

theSum()