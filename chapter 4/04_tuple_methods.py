a = (1,45,342,3432,False,True,3.14,"Hello")
print(type(a)) # print the tuple
print(a) 
n0 =a.count(45)
print(n0) # count the number of 45 in the tuple
n1 = a.index(3.14)
print(n1) # index of 3.14 in the tuple

# Tuples are pretty minimal in terms of built-in methods because of their immutability. **Besides `.count()` and `.index()`, there aren’t any other tuple-specific methods.**

# But you can still do a lot with tuples using **general sequence operations** and Python built-in functions that work with any iterable or sequence.

# ---

# ### Beyond `.count()` and `.index()`, here are useful operations you can do with tuples:

# | Operation           | Description                                  | Example                             |
# | ------------------- | -------------------------------------------- | ----------------------------------- |
# | **Concatenation**   | Join two tuples together to make a new tuple | `(1, 2) + (3, 4)` → `(1, 2, 3, 4)`  |
# | **Repetition**      | Repeat a tuple multiple times                | `(1, 2) * 3` → `(1, 2, 1, 2, 1, 2)` |
# | **Slicing**         | Extract a portion of a tuple                 | `(1, 2, 3, 4)[1:3]` → `(2, 3)`      |
# | **Membership test** | Check if an element exists                   | `3 in (1, 2, 3)` → `True`           |
# | **Length**          | Get number of items                          | `len((1, 2, 3))` → `3`              |
# | **Iteration**       | Loop over elements                           | `for x in (1, 2, 3): print(x)`      |
# | **Unpacking**       | Assign tuple elements to variables           | `a, b, c = (1, 2, 3)`               |

# ---

# ### Built-in functions useful with tuples:

# | Function   | Description                             | Example                       |
# | ---------- | --------------------------------------- | ----------------------------- |
# | `len()`    | Number of elements                      | `len((1, 2, 3))` → `3`        |
# | `max()`    | Largest element                         | `max((1, 4, 2))` → `4`        |
# | `min()`    | Smallest element                        | `min((1, 4, 2))` → `1`        |
# | `sum()`    | Sum of numeric elements                 | `sum((1, 2, 3))` → `6`        |
# | `sorted()` | Returns a sorted list (tuple unchanged) | `sorted((3,1,2))` → `[1,2,3]` |

# ---

# ### Example combining operations:

# ```python
# t1 = (1, 2, 3)
# t2 = (4, 5)

# t3 = t1 + t2        # (1, 2, 3, 4, 5)
# t4 = t3 * 2         # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# print(t4[2:7])      # (3, 4, 5, 1, 2)
# print(5 in t4)      # True
# print(len(t4))      # 10
# ```

# ---

# If you want, I can also explain how tuples compare with lists for specific use cases or how to convert between them!
