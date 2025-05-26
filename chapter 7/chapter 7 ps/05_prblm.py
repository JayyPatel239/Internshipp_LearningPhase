
# 5. Write a program to find the sum of first n natural numbers using while loop. 
i=1
n = int(input("Enter a number: "))
sum = 0
while i <= n:
    sum += i
    i += 1  
    print(f"Sum of first {n} natural numbers is: {sum}")