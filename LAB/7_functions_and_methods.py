#  Practical Example: 1) Write a Python program to print "Hello" using a string.
def print_hello():
    print('Hello')
print_hello()

#  Practical Example: 2) Write a Python program to allocate a string to a variable and print it.
str1="My name is rishu"
def print_str(str1):
    print(str1)

print_str(str1)
#  Practical Example: 3) Write a Python program to print a string using triple quotes.
str2='''Hello
my name is rishu
I am a python programmer
'''
print(str2)
#  Practical Example: 4) Write a Python program to access the first character of a string using
# index value.
str3="Hello my name is rishu"
print(str3[0])
#  Practical Example: 5) Write a Python program to access the string from the second position
# onwards using slicing.
str4="Hello my name is rishu"
print(str4[1:])

#  Practical Example: 6) Write a Python program to access a string up to the fifth character.
str5="Hello my name is rishu"
print(str5[:7])
#  Practical Example: 7) Write a Python program to print the substring between index values 1
# and 4.
str6="Hello world"
print(str6[1:4])
#  Practical Example: 8) Write a Python program to print a string from the last character.
str7="Hello world"
print(str7[-1])
#  Practical Example: 9) Write a Python program to print every alternate character from the
# string starting from index 1.
str8="Hello world"
print(str8[1::2])