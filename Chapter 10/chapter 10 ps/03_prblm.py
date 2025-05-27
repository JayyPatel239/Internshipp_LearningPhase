'''
Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?
'''

class Example:
    a = 5  # class attribute
   
        
# Example usage
obj = Example()
print(f"Before change: {Example.a}")  # Output: 5
obj.a = 0  # Changing the class attribute using the object
print(f"After change: {Example.a}")  # Output: 0
print(f"Object's a: {obj.a}")  # Output: 0

'''
When you do obj.a = 0, Python creates an instance attribute named a for that object.

It does not modify the class attribute Example.a.

The class attribute remains unchanged unless explicitly changed using Example.a = ....
'''