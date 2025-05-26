# #1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!
languages = { 
    "madad:" : "help",
    "shukriya:" : "thank you",
    "namaste:" : "hello",
    "aap kaise hain:" : "how are you",
}
word= input("Enter the word you want meaning of: ")
print(languages[word]) # print the meaning of the word