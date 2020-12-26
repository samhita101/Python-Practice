# prompting the user
print("User, how long do you want your list to be?")
print("Enter how long you want your list to be:")

# users list length and list
list_length = int(input())
number_list = []

# asking the user to input the amount of numbers they wanted and adding them the list
for i in range(list_length):
    print("User enter a number")
    users_num = float(input())
    number_list.append(users_num)

# finding the mean of the list


def mean():
    print(number_list, "is your list.")
    num_list_sum = sum(number_list)
    print(num_list_sum/list_length, "is the mean of your list.")

# calling the function


mean()

