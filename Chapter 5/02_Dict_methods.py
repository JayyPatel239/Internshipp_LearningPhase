marks = {
    "John": 85,
    "Jane": 90,
    "Jim": 78,
    "Jill": 92,
    "Jack": 88,
    "Jenny": 95
}
print(marks.items()) # print the items of the dictionary
print(marks.keys()) # print the keys of the dictionary keys=['John', 'Jane', 'Jim', 'Jill', 'Jack', 'Jenny']
print(marks.values()) # print the values of the dictionaryvalues=98,99
marks.update({"John": 90, "Jay":100}) # update the value of the key "John" to 90 also if values are not dictionary then it will add the key "Jay" with value 100
# print the dictionary after updating the value of the key "John"
print(marks) # print the dictionary after updating the value of the key "John"
print(marks.get("Jay"))#Here it will pribt none if key does not exit
print(marks["Jay"]) #here if key does not exit iyt will show error

print(marks.__len__())

# Sure! Python dictionaries (`dict`) are powerful data structures for storing key-value pairs. Here's a list of the **most commonly used dictionary methods**, with examples:

# ---

# ### 📘 **Common Dictionary Methods**

# | Method                            | Description                                     | Example                |
# | --------------------------------- | ----------------------------------------------- | ---------------------- |
# | `dict.keys()`                     | Returns a view of all keys                      | `d.keys()`             |
# | `dict.values()`                   | Returns a view of all values                    | `d.values()`           |
# | `dict.items()`                    | Returns a view of key-value pairs (tuples)      | `d.items()`            |
# | `dict.get(key)`                   | Returns value for key, or `None` if not found   | `d.get('a')`           |
# | `dict.get(key, default)`          | Returns value or a custom default if missing    | `d.get('x', 0)`        |
# | `dict.pop(key)`                   | Removes and returns the value for the given key | `d.pop('a')`           |
# | `dict.popitem()`                  | Removes and returns the last key-value pair     | `d.popitem()`          |
# | `dict.update(other_dict)`         | Updates with another dictionary                 | `d.update({'x': 5})`   |
# | `dict.clear()`                    | Removes all items from the dictionary           | `d.clear()`            |
# | `dict.copy()`                     | Returns a shallow copy of the dictionary        | `new_d = d.copy()`     |
# | `dict.setdefault(key[, default])` | Sets key to default if not already in dict      | `d.setdefault('k', 0)` |

# ---

# ### 🧪 Example:

# ```python
# d = {'a': 1, 'b': 2, 'c': 3}

# print(d.keys())        # dict_keys(['a', 'b', 'c'])
# print(d.values())      # dict_values([1, 2, 3])
# print(d.items())       # dict_items([('a', 1), ('b', 2), ('c', 3)])
# print(d.get('a'))      # 1
# print(d.get('x', 0))   # 0

# d.update({'d': 4})
# print(d)               # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# d.pop('b')             
# print(d)               # {'a': 1, 'c': 3, 'd': 4}

# d.clear()              
# print(d)               # {}
# ```

# ---

