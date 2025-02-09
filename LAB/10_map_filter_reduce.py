#  Write a Python program to apply the map() function to square a list of numbers.
def square(num):
    return num*2
numbers=[1,2,3,4,5]
result=map(square,numbers)
print(list(result))
#  Write a Python program that uses reduce() to find the product of a list of numbers.
import functools
def multiply(a,b):
    return a*b
numbers1=[1,2,3,4,5]
result1=functools.reduce(multiply,numbers1)
print(result1)

#  Write a Python program that filters out even numbers using the filter() function.

def is_even(num):
    return num%2==0
numbers3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result3=filter(is_even,numbers3)
print(list(result3))