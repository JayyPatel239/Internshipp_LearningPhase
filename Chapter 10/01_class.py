'''
MODELLING A PROBLEM IN OOPS 
We identify the following in our problem. 
• Noun → Class → Employee 
• Adjective → Attributes → name, age, salary 
• Verbs → Methods → getSalary(), increment()
'''
class Employee:
    
    language="PY" #class  attribute
    salary = 100000 # class attribute
    
    
jay=Employee()
jay.name = "Jay"  # instance attribute
print(jay.name, jay.language, jay.salary)     

# Here name is instance attribute, language and salary are class attributes as they directly belong to class
