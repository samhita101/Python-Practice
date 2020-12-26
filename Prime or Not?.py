print("Please enter a number to see if it is prime or composite:")
x = int(input())

if x <= 1:
    print("Neither Prime or Composite")

elif x >= 2:
    for i in range(2, x):
        if x % i == 0:
            print(x, "is composite")
            break

    else:
        print("Prime")
