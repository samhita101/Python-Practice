print("This is a program that is bad at reading.")
print("It stutters some words.")
print("Enter a word that the program will try to read.")
users_word = str(input())

def stutter(x):
    if len(x) <= 2:
        print(x[0], "...", x[0],"...", x, "?")
    else:
        if len(x) > 2:
            print(x[0:2], "...", x[0:2],"...", x, "?")


stutter(users_word)