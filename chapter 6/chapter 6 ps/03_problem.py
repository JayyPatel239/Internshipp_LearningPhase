
# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 
a=input("Enter a comment: ")
if("Make a Lot of Money" in a or "buy now" in a or "Subscribe this" in a or "click this" in a):
    print("Spam comment")
else:
    print("Not a spam comment")
    