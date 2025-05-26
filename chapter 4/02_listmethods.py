l1=[1,3,3,28,9,10,4,8,2]
l1.sort() # sort the list
print(l1) # print the sorted list
l1.reverse() # reverse the list 
print(l1) # print the reversed list
print(l1[-8]) # print the first element of the list
l1.append(100) # append 100 to the list
print(l1) # print the list after appending
l1.insert(2, 200) # insert 200 at index 2   
print(l1) # print the list after inserting
l1.pop(3) # pop the element at index 3
print(l1) # print the list after popping
l1.remove(3)# removing 3 from the list
print(l1) # print the list after removing
l2=l1[::-1] # t\his is a slicing method to reverse the list it doesnt change l1 it returns new list
print(l2) # print the reversed list
l1.clear() # clear the list
print(l1) # print the list after clearing