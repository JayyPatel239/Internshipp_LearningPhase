'''
Repeat program 4 for a list of such words to be censored.
'''
words_to_censor = ["Donkey", "Monkey", "Elephant"]  # List of words to censor
with open("Chapter 9/chapter 9 ps/donkey.txt", "r") as f:
    data = f.read()  # Read the entire file  
for word in words_to_censor:
    data = data.replace(word, "#" * len(word))  # Replace each word with '#####'
with open("Chapter 9/chapter 9 ps/donkey.txt", "w") as f:
    f.write(data)  # Write the updated data back to the file

