f=open("Chapter 9/file.txt")


# lines = f.readlines()
# print(lines,type(lines))

lineq=f.readlines() # Read all lines into a list
print(lineq, type(lineq))
line2=f.readline() # Read the next line 
print(line2, type(line2))
line3=f.readline() # Read the next line
print(line3, type(line3))

f.close()