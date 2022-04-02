gradeList=[]
bucket=0
lowgrade=100
highgrade=0
numGrades=int(input('how many grades? '))
for i in range(0,numGrades,1):
    grade=float(input('please enter your grade: '))
    gradeList.append(grade)
for i in range(0,numGrades,1):
    print(gradeList[i])
for i in range(0,numGrades,1):
    bucket=bucket+gradeList[i]
average=bucket/numGrades
print('Your Average is: ',average)
for i in range(0,numGrades,1):
    if(gradeList[i]<lowgrade):
        lowgrade=gradeList[i]
print ('Your low grade is',lowgrade)
for i in range(0,numGrades,1):
    if(gradeList[i]>highgrade):
        highgrade=gradeList[i]
print('your high grade is',highgrade)  




    