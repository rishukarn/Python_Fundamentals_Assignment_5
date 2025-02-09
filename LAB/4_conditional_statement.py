#  Practical Example 5: Write a Python program to find greater and less than a number using
# if_else.

'''
num_1=int(input('Enter your 1st number: '))
num_2=int(input('Enter your 2nd number: '))

if num_1>num_2:
    print(f'{num_1} is greater than {num_2}')
elif num_1<num_2:
    print(f'{num_1} is less than {num_2}')
else:
    print(f'{num_1} is equal to {num_2}')
'''

#  Practical Example 6: Write a Python program to check if a number is prime using if_else.
'''
numPrime=int(input('Enter a number to check if it is prime or not : '))
flag=0
for i in range(2,numPrime+1):
    if numPrime%i==0:
        flag+=1
if flag>1:
    print(f'{numPrime} is not a prime number')
else:
    print(f'{numPrime} is a prime number')
'''
#  Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.
'''
stu_percentage=float(input('Enter your percentage: '))
if stu_percentage>=90:
    print('Grade +A')
elif stu_percentage >= 80:
    print('Grade A')

elif stu_percentage >= 70:
    print('Grade B')

elif stu_percentage >= 60:
    print('Grade C')

elif stu_percentage >= 50:
    print('Grade D')

else:
    print('F')
'''
        
#  Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.

Gender=input('Enter your gender (M/F): ')

if Gender.upper()=='M':
    Age=int(input('Enter your age: '))
    if Age>=18 and Age<=80:
        print('You are eligible to donate blood')
    else:
        print('You are not eligible to donate blood')
elif Gender.upper()=='F':
    Age=int(input('Enter your age: '))
    if Age>=22 and Age<=60:
        print('You are eligible to donate blood')
    else:
        print('You are not eligible to donate blood')
else:
    print('Invalid gender')