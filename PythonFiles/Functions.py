def tally(x,y):
    z=x+y
    return z

num=5
num2=6
tal=tally(num,num2)
print(tally(num,num2))

def ArrayTally(numNum,myArray):
    tot=0
    for i in range(0,numNum,1):
        tot=tot+myArray[i]
    return tot

number=5
yipyip=[2,4,6,8,10]
mySum=ArrayTally(number,yipyip)
print('array total= ',mySum)


def SumDifProQou(x,y):
    tot=x+y
    dif=x-y
    prod=x*y
    div=x/y
    return tot,dif,prod,div

a=float(input('Enter First Number '))
b=float(input('Enter Second Number '))
w,x,y,z=SumDifProQou(a,b)
print('sum is= ',w)
print('dif is= ',x)   
print('product is= ',y) 
print('qoutient= ',z)

def MyArray(number):
    x=[]
    for i in range(0,number,1):
        myNum=float(input('Enter number '))
        x.append(myNum)
    return x

numnums=int(input('How many numbers '))
y=MyArray(numnums)
print(y)