print("How long do you want your list.")
list_length = int(input())
users_list = []
squares = []
x = 5

for i in range(list_length):
    print("Gimme number:")
    x = int(input())
    users_list.append(x)

print("Here is your list:", users_list)

for k in users_list:
    import math
    sqrt_root = math.sqrt(k)
    if int(sqrt_root) ** 2 == k:
        squares.append(k)
print(squares, "is the list of squares that are in your list.")

