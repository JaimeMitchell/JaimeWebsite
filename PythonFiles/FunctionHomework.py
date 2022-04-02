def inputGrade(nm,grd): #my way. included name of students. that's not what paul did. below is paul's method is more modular.
    nm=int(input('number of students? '))
    gradelist=[]
    namelist=[]
    for i in range(0,nm,1):
        name=str(input('name of student? '))
        namelist.append(name)
        for i in range(0,grd,1):
                grade=float(input('Grades of student? '))
                gradelist.append(grade) 
    return nm,grd,namelist,gradelist
    print('your Grades are: ')
    
#paul's method. he starts with psuedo code. First function only wants to know how many Grades I want to input.
#1. What do we want to do: How many Grades are there. 'numGrades=(input integer number). Ask myself: Does this live in the main program or inside the function? Main
#because user input needs to live in the main program. 
#2. What is the logic to what we want? Input. So we need to input those Grades into the 'myGrades' in MAIN PROGRAM and create a function to capture and return input: 
# myGrades=inputGrades(numGrades). 
#3. Data type for input? Integer since the number of Grades per student is an absolute value.
#3. Logic to input? We need to loop to give it logic magic to bring code alive. 'for i in range(0,nm,1): grd=input('Please enter your grade: '). 
#4. Data type for loop? what kind of data type we want to input. Float.
#5. Then where do we want to put those Grades? An array: (name of array).append (what do i want to append?'grd'): Grades.append(grd) 
# He notes that calling a function, uses (). [] INDEX the array
#6. Need to define the array with a name. Grades=[]
#7. Return Grades[]. Return is the OUTPUT. 'Grades' array is what 'return' function is passing back which will be caught by the MAIN PROGRAM in the array 'myGrades'
# Dont need to add 'nm' because the main program already knows the argument to the function. It's the arraywe want returned.
# 8. Anticipate variables I want to Return. In high grade and low grade thats 2. That means I need to pass two variables to my HighLow function. 

def inputGrades(nm):
    Grades=[]
    for i in range(0,nm,1):
        grd=float(input('Please enter your grade: '))
        Grades.append(grd)
    return Grades
def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i]) 
def Average(nm,x):
    tot=0
    for i in range(0,nm,1):
        tot=tot+x[i]
    Average=tot/nm # We only want to divide the total by the number of items ONCE, so note it's OUTSIDE THE FOR LOOP.
    return Average
def highLow(nm,x):
    hg=0
    lg=100
    for i in range(0,nm,1):
        hg=x[i]>hg
        lg=x[i]<lg
    return hg,lg

numGrades=int(input('How many Grades? '))
myGrades=inputGrades(numGrades) #/ myGrades is a variable that calls our first function, inputGrades, and passes the argument, numGrades, which needs to reside in main program.
print('')
print('Your grades are: ' )
print('')
printGrades(numGrades,myGrades) # Calling the print function. numGrades is nm, myGrades is x
avg=Average(numGrades,myGrades) #variable 'avg; calling my function 'Average'
print('your average is: ',round(avg,1)) #calling the round function to round to the tenth place.
highG, lowG=highLow(numGrades,myGrades) 
print('')
print('your high grade is: ',highG)
print('your low grade is: ',lowG)
  