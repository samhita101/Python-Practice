print("This smiley - :), is worth +1 point.")
print("This smiley - :(, is worth -1 point.")
print("How many happy faces do you want?")
happy_faces = int(input())
print("How many sad faces do you want?")
sad_faces = int(input())
print("Here is the number of happy faces you entered:{0}".format(happy_faces))
print("Here is the number of sad faces you entered:{0}".format(sad_faces))


def value(arg, arg2):
    if happy_faces >= 0 and sad_faces >= 0 and happy_faces == int(happy_faces) and sad_faces == int(sad_faces):
        print(arg * 1 + arg2 * -1, "is the value of your happy faces and sad faces.")
    else:
        print("Invalid sequence.")


value(happy_faces, sad_faces)
