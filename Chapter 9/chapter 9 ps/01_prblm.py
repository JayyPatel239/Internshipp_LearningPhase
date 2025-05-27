#Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

f = open("Chapter 9/chapter 9 ps/poem.txt", "r")  # Open the file in read mode
data = f.read()  # Read the entire file
if "twinkle" in data.lower():  # Check if 'twinkle' is in the text (case insensitive)
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
f.close()  # Close the file