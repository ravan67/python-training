# Write a Python function that takes a list of words and returns the length of the longest one

word_list = ["nikhil", "chetan", "harivans", "raju", "manisha"]

longest_length = 0
longest_word = ""
for word in word_list:
    length = 0

    for alpha in word:
        length += 1

    if length > longest_length:
        longest_length = length
        longest_word = word


print("Longest Length = ",longest_length)
print("longest word = ",longest_word)
