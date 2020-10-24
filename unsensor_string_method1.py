# getting input for vowels/consonants
print("Give me a string with the vowels starred out.")
words = str(input())
print("Print all the starred-out vowels in order from left to right.")
vowels = str(input())

# converting each input to list of characters
words_characters = list(words)
print(words_characters)
vowels_characters = list(vowels)
print(vowels_characters)

# for loop to traverse through words_characters to replace *s with corresponding letter
for i in range(len(words_characters)):
    if words_characters[i] == '*':
        words_characters[i] = vowels_characters[0]
        # removing first character of vowels_characters so that [0] = first character of list
        vowels_characters.remove(vowels_characters[0])
    else:
        continue

print(words_characters)
# converting words_characters to string from list
list_words_char = ''.join(map(str, words_characters))
print(list_words_char)
