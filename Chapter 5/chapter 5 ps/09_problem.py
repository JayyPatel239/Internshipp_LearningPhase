# #Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}
s = {8, 7, 12, "Harry", [1,2]}

print(s)
# #PS D:\python_notes> & C:/Users/Jay/AppData/Local/Programs/Python/Python313/python.exe "d:/python_notes/Chapter 5/chapter 5 ps/09_problem.py"
# Traceback (most recent call last):
#   File "d:\python_notes\Chapter 5\chapter 5 ps\09_problem.py", line 3, in <module>
#     s = {8, 7, 12, "Harry", [1,2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
#we cannot use list as set element as set rewuires all element which are immutable and hashable

