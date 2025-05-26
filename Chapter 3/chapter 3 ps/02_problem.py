#Write a program to fill in a letter template given below with name and date. 
letter = '''  
    Dear <|Name|>, 
    You are selected! 
    <|Date|> 
    '''
    
letter = letter.replace("<|Name|>", "Jay")
letter = letter.replace("<|Date|>", "23 May")
print(letter)