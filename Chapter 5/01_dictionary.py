# PROPERTIES OF PYTHON DICTIONARIES 
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys. 
# 5. It is a collection of key-value pairs.
d ={}# empty dictionary
marks = {
    "John": 85,
    "Jane": 90,
    "Jim": 78,
    "Jill": 92,
    "Jack": 88,
    "Jenny": 95
}
print(marks, type(marks)) # print the dictionary
print(marks["John"]) # print the value of the key "John"
print(marks[0]) # It will give an error because dictionary is not indexed