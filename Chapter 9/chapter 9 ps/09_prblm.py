'''
Write a program to find out whether a file is identical & matches the content of 
another file.
'''
with open("Chapter 9/chapter 9 ps/this.txt", "r") as f:
    content1 = f.read()  # Read the content of the first file

with open("Chapter 9/chapter 9 ps/this_copy.txt", "r") as f_copy:
    content2 = f_copy.read()  # Read the content of the second file

if content1 == content2:  # Compare the contents of both files
    print("The files are identical and match in content.")
else:
    print("The files are not identical; they do not match in content.")