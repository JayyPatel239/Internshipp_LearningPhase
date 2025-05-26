
# 6. Write a python function which converts inches to cms. 
def inches_to_cms(inches):
    return inches * 2.54

inches= float(input("ENTER A NUMBER IN INCHES: "))
print(f"{inches} inches is equal to {inches_to_cms(inches)}")