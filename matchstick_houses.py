# collecting input
print("What is your step value?")
step = int(input())


# defining function to count number of matchsticks
def matchsticks_num(arg):
    while step == int(step) and step >= 0:  # allows only integer values and positive numbers
        print(1 + 5*arg, "is the number of matchsticks in your step.")


# calling the function
matchsticks_num(step)
