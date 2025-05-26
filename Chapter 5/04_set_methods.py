s={1, 5 , 6 , 7, 8, 9}

s.add(10) # add 10 to the set

print(s) # print the set

s.remove(5) # remove 5 from the set
print(s) # print the set
s.pop() # remove a random element from the set
print(s) # print the set



# ---

# ### 🔹 **Common Python Set Methods**

# | Method                               | Description                                     | Example                                       |                        |      |
# | ------------------------------------ | ----------------------------------------------- | --------------------------------------------- | ---------------------- | ---- |
# | `add(elem)`                          | Adds an element to the set                      | `s.add(10)`                                   |                        |      |
# | `remove(elem)`                       | Removes element, raises error if not found      | `s.remove(5)`                                 |                        |      |
# | `discard(elem)`                      | Removes element if present (no error if absent) | `s.discard(5)`                                |                        |      |
# | `pop()`                              | Removes and returns a random element            | `s.pop()`                                     |                        |      |
# | `clear()`                            | Removes all elements from the set               | `s.clear()`                                   |                        |      |
# | `copy()`                             | Returns a shallow copy                          | `s2 = s.copy()`                               |                        |      |
# | `union(other)` or \`                 | \`                                              | Returns a new set with all elements from both | `s1.union(s2)` or \`s1 | s2\` |
# | `intersection(other)` or `&`         | Elements common to both sets                    | `s1 & s2` or `s1.intersection(s2)`            |                        |      |
# | `difference(other)` or `-`           | Elements in `s1` but not in `s2`                | `s1 - s2`                                     |                        |      |
# | `symmetric_difference(other)` or `^` | Elements in one set or the other, but not both  | `s1 ^ s2`                                     |                        |      |
# | `isdisjoint(other)`                  | True if sets have no elements in common         | `s1.isdisjoint(s2)`                           |                        |      |
# | `issubset(other)`                    | True if set is a subset of another              | `s1.issubset(s2)`                             |                        |      |
# | `issuperset(other)`                  | True if set is a superset of another            | `s1.issuperset(s2)`                           |                        |      |
# | `update(...)`                        | Add elements from another iterable/set          | `s1.update([7, 8])`                           |                        |      |

# ---

# ### 🧪 Example:

# ```python
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}

# s1.add(6)                     # {1, 2, 3, 6}
# s1.discard(2)                # {1, 3, 6}
# print(s1 | s2)               # union → {1, 3, 4, 5, 6, 2}
# print(s1 & s2)               # intersection → {3}
# print(s1 - s2)               # difference → {1, 6}
# print(s1 ^ s2)               # symmetric difference → {1, 4, 5, 6}
# ```

# ---
