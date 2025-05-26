def greet(name = "stranger"):
# function body 
    print(f"Hello {name}, Good Morning!")
    return name
greet() # name will be "stranger" in function body (default) 
greet("jay") # name will be "harry" in function body (passed) 