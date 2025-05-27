'''
Write a class “Calculator” capable of finding square, cube and square root of a 
number. 
'''
class Calculator:
    def square(self,number):
        return number **2
    def cube(self,number):
        return number **3
    def square_root(self,number):
        return number **0.5
    def __str__(self):
        return "This is a Calculator class capable of finding square, cube and square root of a number."
    
# Example usage
calc =  Calculator()
print(calc.square(4))        # Output: 16
print(calc.cube(3))          # Output: 27       
print(calc.square_root(16))  # Output: 4.0
print(calc)  # Output: This is a Calculator class capable of finding square, cube and square root of a number.