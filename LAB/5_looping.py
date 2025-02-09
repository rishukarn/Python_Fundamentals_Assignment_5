#  Practical Example 1: Write a Python program to print each fruit in a list using a simple for
# loop. List1 = ['apple', 'banana', 'mango']
'''
List1 = ['apple', 'banana', 'mango']

for i in List1:
    print(i)
'''
#  Practical Example 2: Write a Python program to find the length of each string in List1.
'''
List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(len(fruit))

'''
#  Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.
'''
List1 = ['apple', 'banana', 'mango']
findSpecific=input('Enter a fruit name fine in the list: ')
for fruit in List1:
    if fruit==findSpecific:
        print(fruit,'is found in List.')
    else:
        print(findSpecific,'is not found in List.')
'''
#  Practical Example 4: Print this pattern using nested for loop:

user=int(input('Enter a number to print the pattern: '))
for i in range(1,user+1):
    for j in range(i):
        print('*', end='')
    print('')