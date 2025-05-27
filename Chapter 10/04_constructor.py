'''
__init__() is a special method which is first run as soon as the object is created. 
__init__() method is also known as constructor. 
It takes ‘self’ argument and can also take further arguments. 
'''
class Employee:
    
    language="PY" #class  attribute
    salary = 100000 # class attribute
    def __init__(self,name,salary,language):  # constructor with parameters
        self.name = name    
        self.salary = salary
        self.language = language
        print("Constructor called, object created!")
    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod   
    def greet():
        print("Hello, welcome to the Employee class!") #static method is a decorator show self para,mater is not required
jay=Employee("Jay", 110000, "Java")  # Creating an instance of Employee with parameters
#jay.name = "Jay"  # instance attribute
print(jay.name,jay.language, jay.salary)  # Accessing class attributes



#the methods starting with double underscore are called magic or dunder methods.