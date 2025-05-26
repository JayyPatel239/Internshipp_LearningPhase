for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # exits the loop when i is 5 riight now
    print(i)
    
for i in range(100):
    if i == 34:
       continue  # skips the rest of the loop when i is 34 it will skip this value and continue with the next iteration
    print(i)
    
