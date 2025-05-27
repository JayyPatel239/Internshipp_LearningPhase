'''
 Write a python program to rename a file to “renamed_by_ python.txt.

'''

import os
# Define the old and new file names
old_file_name = "Chapter 9/chapter 9 ps/this_copy.txt"  
new_file_name = "Chapter 9/chapter 9 ps/renamed_by_python.txt"
# Rename the file
os.rename(old_file_name, new_file_name)
print(f"File renamed from '{old_file_name}' to '{new_file_name}'")
# Check if the file was renamed successfully
if os.path.exists(new_file_name):
    print(f"'{new_file_name}' exists.") 