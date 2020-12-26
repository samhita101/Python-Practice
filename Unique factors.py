print("User, today we will find the number of unique factors your number has.")
print("User give me a positive integer greater than 1:")
number = int(input())
factor_list = []


def prime(arg):
    counter = 1
    if arg <= 1:
        print("Please enter a number greater than one.")

    elif arg >= 2 and arg % 2 == 0:
        for i in range(1, (arg // 2) + 1):
            if arg % i == 0:
                factor_list.append(i)
                counter = counter + 1
        print("There are", counter, "unique factors.")
        factor_list.append(arg)
        print("Here is a list with the factors:", factor_list)

    else:
        if arg >= 2 and arg % 2 != 0:
            for i in range(1, (arg - 1 // 2)):
                if arg % i == 0:
                    factor_list.append(i)
                    counter = counter + 1
            print("There are", counter, "unique factors.")
            factor_list.append(arg)
            print("Here is a list with the factors:", factor_list)


prime(number)
