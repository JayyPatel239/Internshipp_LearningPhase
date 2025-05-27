#Create a class “Programmer” for storing information of few programmers working at Microsoft. 
class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
    
    
p = Programmer("Alice", 30, "C#")
print(f"Name: {p.name}, Age: {p.age}, Language: {p.language}, Company: {p.company}")
        