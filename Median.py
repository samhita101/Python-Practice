print("Today we will be finding the median of a list.")
print("User enter a length for your list:")

# users list length and list
list_length = int(input())
number_list = []

# asking the user to input the amount of numbers they wanted and adding them the list
for i in range(list_length):
    print("User enter a number:")
    users_num = float(input())
    number_list.append(users_num)

# creating a function to find median

def median():
    remainder = list_length % 2  # finds remainder
    print(remainder)
    sorted_list = sorted(number_list)  # sorts list
    print(sorted_list, "is your list sorted in ascending order")
    if remainder == 1:   # if remainder = 1, slices at halfway point, and prints
        slice_position = (list_length + 1)//2 - 1
        print(sorted_list[slice_position], "is the median of your list")
    if remainder == 0:  # if remainder = 0, slices at 2 positions - half and half + 1
        sorted_list = sorted(number_list)  # sorts list
        slice_position2 = list_length/2
        median1 = sorted_list(slice_position2)
        median2 = sorted_list(slice_position2 - 1)
        print((median1 + median2)/2)

median()