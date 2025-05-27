'''
A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.  

'''

word="Donkey"
with open("Chapter 9/chapter 9 ps/donkey.txt", "r") as f:
    data = f.read()  # Read the entire file

data =data.replace(word, "#####")  # Replace 'Donkey' with '#####'
with open("Chapter 9/chapter 9 ps/donkey.txt", "w") as f:
    f.write(data)  # Write the updated data back to the file