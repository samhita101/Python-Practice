print("user, we will create a rectangle with this: *")
print("user, give a number for the row count.")
r = int(input())
print("User give a number for the column count.")
c = int(input())

print("* " * c)
for i in range(r-2):
    print("*", " " * c, "*")
print("* " * c)
