#if-else statement ladder
a= int(input("Enter your age: "))
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