 
# 4. Write a recursive function to calculate the sum of first n natural numbers. 
'''
sum of first n natural numbers = n + (n-1) + (n-2) + ... + 1
'''
def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n-1)

# Test the function
n = int(input("ENTER A NUMBER: "))
result = natural_sum(n)
print(f"The sum of the First {n} Natural Number is:{result}")
    