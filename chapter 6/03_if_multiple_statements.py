#Multiple if-else statement ladder
a= int(input("Enter your age: "))
#if statement 1
if(a%2==0):
    print("a is even")
    #end of if statement 1
#if statement 2 
if(a>=18):
    print("You are eligible to vote")
    print("Make sure to carry your ID card")
elif(a<0):
    print("Invalid age")
elif(a>=0 and a<18):
    print("You are not eligible to vote you are child")
    print("You can vote when you turn 18") 
else:
    print("You are not eligible to vote")
#end of if statement 2
print("This is the end of the program")