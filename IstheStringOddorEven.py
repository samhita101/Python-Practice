print("give me a string")
string_input = str(input())


def length_odd_even(arg):
    if len(arg) % 2 == 0:
        print("you string is even.")
    else:
        print("your string is odd.")


length_odd_even(string_input)
