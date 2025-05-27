f=open("Chapter 9/file.txt")
print(f.read()) # Read the entire file
f.close() # Close the file


#this same above task can be written using with ststaement
with open("Chapter 9/file.txt") as f: # Open the file in read mode
    print(f.read()) # Read the entire file
    
    
#you don't need to close the file explicitly when using with statement
# The file is automatically closed when the block is exited