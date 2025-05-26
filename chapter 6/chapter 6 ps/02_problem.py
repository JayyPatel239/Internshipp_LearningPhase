 
# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

a=int(input("Enter marks of subject 1: "))
b=int(input("Enter marks of subject 2: "))
c=int(input("Enter marks of subject 3: "))

total_marks = a + b + c
total_marks = total_marks / 3 
total_marks = total_marks * 100 / 100
print("Total marks: ", total_marks)  
if total_marks >= 40 and a >= 33 and b >= 33 and c >= 33:
    print("You have passed")
else:
    print("You have failed")