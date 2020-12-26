# prompting the user/collecting input
print("User we will find the perimeter of a rectangle.")
print("User give me a value for length:")
length = float(input())
print("User give me a value for width:")
width = float(input())


# defining the function

def perimeter():
    print(2*length + 2*width)


# calling the function
perimeter()
