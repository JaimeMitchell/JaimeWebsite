gradelist=[]

number=int(input('number?'))

for i in range(0,number,1):
    grade=float(input('grade?'))
    gradelist.append(grade)

for i in range(0,number-1,1): # needs to be one less in order to not go beyond the range of 'number'. 1st loop is the first switch condition that occurs, but it would stop there if not for the next for loop.
    for i in range(0,number-1,1): # Nested for loop ensures the switching occurs with all numbers, not just the first time the condition is true/false.
        if gradelist[i]<gradelist[i+1]: # If 'Current i' is less than the 'Next i' in the array
            swap=gradelist[i] # set temporary variable In order to avoid breaking switch (first low number will replace ever one it's compared to.
                              # Placement of the variable after conditional statement, and before switch, is important because if I initialize before the switch breaks in the same way as above (no swap variable).
            gradelist[i]=gradelist[i+1] #the current i equals the i that comes after it and,
            gradelist[i+1]=swap # The i that comes after the current i becomes the current i, swapping position by swapping identities.


print('Sorted list')
print (gradelist)
for i in range(0,number,1):
    print(gradelist[i])