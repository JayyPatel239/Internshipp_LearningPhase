# #Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os


path = '.'  


dir_list = os.listdir(path)

print(f"Contents of the directory '{path}':")
for item in dir_list:
    print(item)
