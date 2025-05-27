'''
Write a program to make a copy of a text file “this. txt” 
'''

with open("Chapter 9/chapter 9 ps/this.txt", "r") as f:
    content = f.read()  # Read the entire file

with open("Chapter 9/chapter 9 ps/this_copy.txt", "w") as f_copy:
    f_copy.write(content)  # Write the content to the new file