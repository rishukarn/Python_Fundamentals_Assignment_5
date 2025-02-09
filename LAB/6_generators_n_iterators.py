#  Write a generator function that generates the first 10 even numbers.


def even_numbers():
    for i in range(1, 11):
        yield i * 2


evens = even_numbers()
print(evens.__next__)
print(list(evens))
#  Write a Python program that uses a custom iterator to iterate over a list of integers.

numbers_list = [1, 2, 3, 4, 5]
for i in numbers_list:
    print(i)