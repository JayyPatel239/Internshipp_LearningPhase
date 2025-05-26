# Check that a tuple type cannot be changed in python.
a = (1, 2, 3, 4, 5)
print(type(a)) # print the tuple
a[0]=10
print(a) # print the tuple
# a[0] = 10 # this will raise an error because tuples are immutable