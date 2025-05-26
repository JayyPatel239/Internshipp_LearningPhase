'''
a =12
b=45
c=56

average = (a + b + c) / 3
print(f"The average of {a}, {b}, and {c} is: {average}")
'''
#function Definition
def calculate_average():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average = (a + b + c) / 3
    print(f"The average of {a}, {b}, and {c} is: {average}")
    

calculate_average() # function call
# Output: The average of 12, 45, and 56 is: 37.666666666666664