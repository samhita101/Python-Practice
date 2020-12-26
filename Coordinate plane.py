print("Today we will build a coordinate plane with your numbers.")
print("User, give me an x coordinate value.")
x = int(input())
print("User give me a y coordinate value.")
y = int(input())

# for loop to print the number of |'s

if x > 0 and y > 0:
    for i in range(y):
        print("|")
# print statement with multiplication of _
    print("- "*x)

else:
    print("Give me a POSITIVE number please.")