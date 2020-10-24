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

# defining temporary variable
temp_var = -1

# for loop to traverse through words_characters to replace *s with corresponding letter
for i in range(len(words_characters)):
    if words_characters[i] == '*':
        temp_var = (temp_var + 1)  # adding one to temp var so that next character will be used
        words_characters[i] = vowels_characters[temp_var]
        # replacing '*' with corresponding character from vowels_characters
        words_characters[i].replace(words_characters[i], vowels_characters[temp_var])
    else:
        continue

print(words_characters)
# converting words_characters from list to string
list_words_char = ''.join(map(str, words_characters))
print(list_words_char)

