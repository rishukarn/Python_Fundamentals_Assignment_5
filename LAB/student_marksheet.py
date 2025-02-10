
def student_data(name,rollno,*data):
    print(f'\n Student name is : {name}\n Student rollno is : {rollno}')
    # print(data[0])

    grade=0
    for i in data:
        grade+=i
    if grade>=90:
        print(f'\n\n\nStudent grade is A\n per :{grade/5}')
    elif grade>=75:
        print(f'\n\n\nStudent grade is B\n per :{grade/5}')
    elif grade>=60:
        print(f'\n\n\nStudent grade is C\n per :{grade/5}')
    else:
        print(f'\n\n\nStudent grade is f\n per :{grade/5}')
    # print(grade)

list1=[]
name=input('Enter your name: ')
rollno=int(input('Enter your rollno: '))
for i in range(5):
    marks=int(input(f'Enter your marks for subject {i+1}: '))
    list1.append(marks)
student_data(name,rollno,*list1)


        
