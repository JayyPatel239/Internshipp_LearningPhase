#  If languages of two friends are same; what will happen to the program in problem 6? 

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
# PS D:\python_notes> & C:/Users/Jay/AppData/Local/Programs/Python/Python313/python.exe "d:/python_notes/Chapter 5/chapter 5 ps/08_problem.py"
# Enter the name of friend : jay
# Enter the favorite language of friend : pp
# Enter the name of friend : ke
# Enter the favorite language of friend : pp
# Enter the name of friend : ni
# Enter the favorite language of friend : nim
# Enter the name of friend : pan
# Enter the favorite language of friend : ma
# {'jay': 'pp', 'ke': 'pp', 'ni': 'nim', 'pan': 'ma'}
#nothing will be happend values ccan be same
