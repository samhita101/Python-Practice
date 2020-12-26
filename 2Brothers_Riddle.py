answer = 2
wrong1 = 1
wrong3 = 3

print("THE RIDDLE:")
print("You are walking down a path when you come to two doors.")
print("Opening one of the doors will lead you to a life of prosperity and happiness, \nwhile opening the other door will lead to a life of misery and sorrow.")
print("You don't know which door leads to which life.")
print("In front of the doors are two twin guard brothers who know which door leads where.")
print("One of the brothers always lies, and the other always tells the truth.")
print("You don't know which brother is the liar and which is the truth-teller.")
print("You are allowed to ask one single question to one of the brothers (not both) to figure out which door to open.")
print("What question should you ask?")
print("")
print("YOUR CHOICES:")
print("1. You should ask either brother which door leads to a life of happiness and prosperity.")
print("2. You should ask either brother which door the other would pick if I asked them which leads to a life of happiness and prosperity.")
print("3. You should ask the truthful brother which door leads to a life of misery and sorrow.")
print("")
print("Pick one of the choices and enter the number that corresponds with the question you want to ask either brother:")
guess = int(input())
print("")
if guess == answer:
    print("Correct.\nIf you were to ask the truthful brother which door his brother would pick,\nhe would point to the door that leads to misery and sorrow since that is what his brother would pick.\nIf you asked the lying brother which door his sibling would pick,\nhe will also point to the bad door,\nbecause this is not what his brother would point to.")
    print("So whichever door is pointed to, you should go through the opposite.")
elif guess == wrong1:
    print("Incorrect. If you were to ask the liar which door leads to a life of happiness and prosperity,\nhe would point to the oppsite of what his brother would point to.\nThis makes it impossible to know which is the right door, since they're each pointing at a different door.")
else:
    guess == wrong3
    print("Incorrect.If you were to ask the liar which door leads to a life of misery and sorrow,\nhe would point to the oppsite of what his brother would point to.\nThis makes it impossible to know which is the right door, since they're each pointing at a different door.")
