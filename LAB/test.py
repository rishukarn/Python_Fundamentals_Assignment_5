# name="rishu is good"
# print(name[::2])


# def Table(num):
#     for i in range(1,11):
#         print(f'{num} X {i} = {num*i}')

# user=int(input('Enter a number: '))
# Table(user)


def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact*=i
    print(fact)



user = int(input('Enter a number: '))
factorial(user)
