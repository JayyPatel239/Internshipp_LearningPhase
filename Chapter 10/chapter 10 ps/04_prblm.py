#Add a static method in problem 2, to greet the user with hello. 

class Demo:
    def __init__(self):
        print("Demo class initialized!")

    @staticmethod
    def greet():
        print("Hello, welcome to the Demo class!")  # Static method does not require 'self'
        
# Example usage
demo_instance = Demo()  # Creating an instance of Demo
demo_instance.greet()  # Calling the static method using the instance