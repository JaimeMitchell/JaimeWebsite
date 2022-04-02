grade=97
grade=98
grade3=76
print(grade)
grades=[97,98,76,54,99,85,67]
print(grades)
print(grades[2])

x=grades[0]+grades[2]
print(x)

picture=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(picture)
print(picture[0])
print(picture[1])
print(picture[2])
print(picture[1][2])

fruits=['apple','banana','orange','grape']
print(fruits)
print(fruits[1])

grades=[97,34,23,99,'banana',100]
print(grades)
print(grades[0])
print(grades[4])
print(grades[4][0])

x=97
y=34
z=23
a=99
b=100
c=101
grades=[x,y,z,a,b,c]
print(grades)
grades=['x','y','z','a','b','c']
print(grades)
fruits=['apple','banana','orange','grape','kiwi']
print(fruits[1][2])
print(fruits[2][0])
print(fruits[0][1])
print(fruits[0][4])
print(fruits[1:5])

grades=[97,98,76,54,99,85,67]
grades[0]=25
print(grades)

x=[]
print(x)
x.append(97)
print(x)
x.append(85)
print(x)

fruit=['apple','Orange','banana','apricot','mango']
print(fruit[0:5])

x=7
y=2
z=x+y
print(x,'+',y,'=',z)

x=input('please input a number: ')
print('your number is ',x)
name=input('Please enter your name: ')
print('Hello, ',name,',welcome to Python Land.')

x=input('give a number: ')
y=input('give another number: ')
x=float(x)
y=float(y)
z=x+y
print(x,'+',y,'=',z)

x=int(input('give a number: '))
y=int(input('give another number: '))
z=x+y
print(x,'+',y,'=',z)

myNumber=float(input('Please input your number: '))
if(myNumber==7):
    print('Yep')
if(myNumber<7):
    print('Nope')   
if(myNumber>7):
    print('WTF is this?')
    
urNumber=int(input('What is your number: '))
if(urNumber%2==0):
    print('Your number is even.')         
else:
    print('Your number is odd.')
    
num=float(input('Gimme number: '))
rem=num%2
if(rem==0):
    print('You have an even number')
if(rem==1):
    print('You have an odd number')
    
myColor=input('Color?: ')
if(myColor=='Red' or myColor=='red' or myColor=='RED'):
    print('your color is red')
if(myColor!='Red'and myColor!='red'and myColor!='RED'):
    print('YOUR COLOR IS NOT RED')
 
urNum=float(input('gimme number 1-10: '))    
if(urNum>=1 and urNum<=10):
    print('right on')
if(urNum<1 or urNum>10):
    print('WTF did i say?')


    
        
   