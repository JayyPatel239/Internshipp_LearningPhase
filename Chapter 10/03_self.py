'''
self refers to the instance of the class. It is automatically passed with a function call 
from an object. 
'''

class Employee:
    
    language="PY" #class  attribute
    salary = 100000 # class attribute
    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod   
    def greet():
        print("Hello, welcome to the Employee class!") #static method is a decorator show self para,mater is not required
jay=Employee()

jay.language = "Java"  # changing class attribute for this instance
# print(jay.language, jay.salary)   
jay.getinfo()  # This will raise an error because getinfo is not defined as an instance method
#Employee.getinfo()  # This will also raise an error because getinfo is not defined as a class method
# To fix this, we need to define getinfo as an instance method by adding 'self' as the first parameter. 

jay.greet() 
