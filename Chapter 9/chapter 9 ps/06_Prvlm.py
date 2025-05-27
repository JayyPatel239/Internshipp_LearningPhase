'''
Write a program to mine a log file and find out whether it contains ‘python’. 
'''
with open("Chapter 9/chapter 9 ps/log.txt", "r") as f:
    data = f.read()  # Read the entire file
    if "python" in data.lower():  # Check if 'python' is in the text (case insensitive)
        print("The word 'python' is present in the log file.")
    else:
        print("The word 'python' is not present in the log file.")