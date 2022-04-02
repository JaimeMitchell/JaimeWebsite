import pickle
with open('STU.pkl','rb') as stud:
    inputGrade=pickle.load(stud)
while(1==1):
    name=input('Which student do you want to check? ')
    for i in range(0,numStu,1):
        if (names[i]==name):
            print(str(name)+"'s grade is "+str(grades[i])+'.')