# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']

List1=['apple', 'banana', 'mango']
for i in List1:
    if i=="banana":
        continue
    print(i)
#  Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
# the break statement.

for i in List1:
    if i=="banana":
        print("banana is found")
        break
    

