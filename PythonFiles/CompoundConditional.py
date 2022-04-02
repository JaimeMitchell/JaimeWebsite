n=float(input('n?: '))
if(n==0):
    print('0')
if(n%2==0 and n> 0):
    print('positive even')
if(n%2==0 and n< 0):
    print('negative even')
if(n%2==1 and n> 0):
    print('positive odd')
if(n%2==1 and n< 0):
    print('negative odd')

n=float(input('Enter nber:'))
rem=n%2
if(n>=1 and rem==0):
    print('positive even')
if(n>=1 and rem==1):
    print('positive odd')
if(n<0 and rem==0):
    print('negative even')
if(n<1 and rem==1):
    print('negative odd')
if(n==0):
    print('Zero')
    
n=float(input('Input number: '))
rem=n%2
if (n>0 and rem==0):
    print('Even Positive')
if(n>0 and rem==1):
    print('Odd Positive')
if(n<0 and rem==0):
    print('Even Negative')
if(n<0 and rem==1):
    print('Odd Negative')
if(n==0):
    print('Zero')
