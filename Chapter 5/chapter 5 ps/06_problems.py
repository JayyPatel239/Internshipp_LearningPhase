#Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
s={}

name=input("Enter the name of friend : ")
language=input("Enter the favorite language of friend : ")
s.update({name:language})
name=input("Enter the name of friend : ")
language=input("Enter the favorite language of friend : ")
s.update({name:language})
name=input("Enter the name of friend : ")
language=input("Enter the favorite language of friend : ")
s.update({name:language})
name=input("Enter the name of friend : ")
language=input("Enter the favorite language of friend : ")
s.update({name:language})
print(s)
