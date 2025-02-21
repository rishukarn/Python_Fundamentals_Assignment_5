# name="rishu is good"
# print(name[::2])


# def Table(num):
#     for i in range(1,11):
#         print(f'{num} X {i} = {num*i}')

# user=int(input('Enter a number: '))
# Table(user)


# def factorial(num):
#     fact=1
#     for i in range(num,1,-1):
#         fact*=i
#     print(fact)



# user = int(input('Enter a number: '))
# factorial(user)


# s1={10,20,30,40,50}
# s2={20,60,70,40,80}
# print(s1-s2)
# print(s2.difference(s1))


# s1={10,10}
# print(s1)

# lsit=[1,1,3,5,6,7,4,5]
# print(set(lsit))

data={
    'id':'1234',
    'name':'Rishu',
    'course':'python',
    'per':50

}

if data['per']<40:
    print('fail')
else:
    print('pass')


# palindrome=input('Enter a string to check palindrome:')
# if palindrome==palindrome[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')

# lst=[]
# for i in range(5):
#     user=int(input('Enter a number: '))
#     lst.append(user)
# new_lst=max(lst)
# new2_lst=min(lst)
# print(f'In this list {new_lst} is max number')
# print(f'In this list {new2_lst} is min number')


def filte_number(num):
    return num%3==0 or num%5==0


numbers3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result3=filter(filte_number,numbers3)
print(list(result3))
    
