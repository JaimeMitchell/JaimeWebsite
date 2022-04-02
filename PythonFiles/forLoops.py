fruits=['apple','orange','banana','mango','kiwi']
for fruit in fruits:
    print(fruits)
for fruit in fruits:
    print(fruit)
    for letter in fruit:
        print(letter)
print("that's all folx")

for fruit in fruits:
    for letter in fruit:
        print(letter)
print("this is how to branch for loops")

myNums=[1,2,3,4,5,6,7,8,9,10]
for myNum in myNums:
    print(myNum)

for myNumber in range(1,10,1):
    print(myNumber)

for myNumber in range(0,1000,100):
    print(myNumber)

for myNumber in range(10,-1,-1):
    print(myNumber)

    number=int(input('input amount of grades: '))
grades=[]
for counter in range(0,number,1):
    grade=float(input('input specific grade: '))
    grades.append(grade)
    print(grades)
for grade in grades:
    print (grade)

gradelist=[]
num=int(input("INPUT YOUR NUMBER OF GRADES: "))
for i in range(0,num,1):
    grade=float(input('enter your grades: '))
    gradelist.append(grade)
    print(gradelist)
    print(grade)
print('your grades are:')
for i in range(0,num,1):
    print(gradelist[i])

grades=[]
numGrades=int(input('How many grades do you have? '))
for i in range(0,numGrades,1):
    grade=float(input('Please enter your grade: '))
    grades.append(grade)
print('Your grades are:')
for i in range(numGrades):
    print(grades[i])

num=int(input('How many grades do you have?')) 
grades=[]
bucket=0
for i in range(0,num,1):
    grade=float(input('enter grades: '))
    grades.append(grade)
print('')   
print('Your grades are ')
print(grades[i])

for i in range(0,num,1):
    bucket=bucket+grades[i]
average=bucket/num
print('')
print('your average is: ',average)
for i in range(0,num,1):
    grades[i]

