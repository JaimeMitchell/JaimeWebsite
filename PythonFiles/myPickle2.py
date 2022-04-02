import pickle
with open('studentData.pkl','rb') as stuL:
    numStu=pickle.load(stuL)
    names=pickle.load(stuL)
    grades=pickle.load(stuL)
while(1==1):
    name=input('Which student do you want to check? ')
    for i in range(0,numStu,1):
        if (names[i]==name):
            print(str(name)+"'s grade is "+str(grades[i])+'.')