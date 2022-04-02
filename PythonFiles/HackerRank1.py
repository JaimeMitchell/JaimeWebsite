n=float(input('Enter number: '))
rem=n%2
if (n>=1 and n<=5 and rem==0):
    print("Not Weird")
if (n>=6 and n<=20 and rem==0):
    print('Weird')
if (n>=21 and n<=100 and rem==0):
    print('Not Weird')
if (n>=1 and n<=100 and rem==1):
    print("Weird")
if(n<=0 or n>100):
    print("Out of bounds!")