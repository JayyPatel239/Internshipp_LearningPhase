# 1. Write a program using functions to find greatest of three numbers. 
def greatest_of_3_numbers(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Call the function and print the result
result = greatest_of_3_numbers(num1, num2, num3)
print(f"The greatest of {num1}, {num2}, and {num3} is: {result}")