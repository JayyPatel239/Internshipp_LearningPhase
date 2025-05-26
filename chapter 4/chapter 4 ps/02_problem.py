# Write a program to accept marks of 6 students and display them in a sorted manner. 

marks=input("Enter the marks of 6 students separated by commas: ")
marks=marks.split(",")
marks.sort()
print(marks)