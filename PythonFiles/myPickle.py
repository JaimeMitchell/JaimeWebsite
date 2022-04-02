import pickle
names=[]
grades=[]
num=int(input('Please input # students: '))
for j in range(0,num,1):
    name=(input("Please input student name: "))
    names.append(name)
    prompt='Please enter'+name+"'s grade: "
    grade=float(input(prompt))
    grades.append(grade)
with open('studentData.pkl','wb') as stuD:
    pickle.dump(num,stuD)
    pickle.dump(names,stuD)
    pickle.dump(grades,stuD)
with open('studentData.pkl','rb') as stuL:
    a=pickle.load(stuL)
    b=pickle.load(stuL)
    c=pickle.load(stuL)
print(a)
print(b)
print(c)
    

