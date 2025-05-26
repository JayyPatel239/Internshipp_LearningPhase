# # What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?

s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# When you compare them using ==:

# Python converts 20 to 20.0

# Then compares 20.0 == 20.0

# So the result is True so that's why the length of the set is 2

