# collecting input from user
print("Give me a value for the length of your list")
list_length = int(input())
print("Give me a value for the number you want your multiples based off of.")
multiple_base = int(input())


def list_of_multiples(num, length):
    multiples_list = []
    for i in range(1, length+1):
        multiples_list.append(num*i)
    print(multiples_list)


list_of_multiples(multiple_base, list_length)
