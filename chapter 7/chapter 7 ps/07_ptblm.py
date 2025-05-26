
# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 

'''
    * 
   ***
  *****
 *******
*********
for n =5
'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(f"{' ' * (n - i)}{'*' * (2 * i - 1)}")

