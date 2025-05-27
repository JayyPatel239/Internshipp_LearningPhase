class Employee:
    
    language="PY" #class  attribute
    salary = 100000 # class attribute
    
    
jay=Employee()

jay.language = "Java"  # changing class attribute for this instance
print(jay.language, jay.salary)     


# Instance attributes, take preference over class attributes during assignment & retrieval. 
