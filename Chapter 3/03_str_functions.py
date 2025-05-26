name ="Jay Patel"

print(len(name))
print(name.endswith("tel"))

print(name.startswith("Ja"))
print(name.capitalize()) # if input is jay, output is Jay   and it will change only the first word next word will not capitalize

print(name.find("Patel")) # it will give the index of the first letter of the word
replacedname=name.replace("Jay", "Akshar") # it will replace the first word with the second word
print(replacedname)



#🔤 String Methods in Python
# Method	Description	Example
# str.lower()	Converts string to lowercase	'HELLO'.lower() → 'hello'
# str.upper()	Converts string to uppercase	'hello'.upper() → 'HELLO'
# str.title()	Capitalizes the first letter of each word	'hello world'.title() → 'Hello World'
# str.strip()	Removes leading/trailing whitespace	' hello '.strip() → 'hello'
# str.lstrip()	Removes leading whitespace	' hello'.lstrip() → 'hello'
# str.rstrip()	Removes trailing whitespace	'hello '.rstrip() → 'hello'
# str.replace(old, new)	Replaces all occurrences	'aabb'.replace('a', 'x') → 'xxbb'
# str.split(sep)	Splits string into a list	'a,b,c'.split(',') → ['a', 'b', 'c']
# str.join(list)	Joins list elements into a string	','.join(['a', 'b']) → 'a,b'
# str.find(sub)	Returns lowest index of substring or -1	'hello'.find('e') → 1
# str.index(sub)	Like find() but raises error if not found	'hello'.index('e') → 1
# str.startswith(prefix)	Checks if string starts with prefix	'hello'.startswith('he') → True
# str.endswith(suffix)	Checks if string ends with suffix	'hello'.endswith('lo') → True
# str.count(sub)	Counts occurrences of substring	'banana'.count('a') → 3
# str.isalpha()	Returns True if all chars are alphabetic	'abc'.isalpha() → True
# str.isdigit()	Returns True if all chars are digits	'123'.isdigit() → True
# str.isalnum()	Returns True if all chars are alphanumeric	'abc123'.isalnum() → True
# str.isspace()	Returns True if all chars are whitespace	' '.isspace() → True
# str.capitalize()	Capitalizes first character only	'hello'.capitalize() → 'Hello'
# str.zfill(width)	Pads string with zeros on the left	'42'.zfill(5) → '00042'
