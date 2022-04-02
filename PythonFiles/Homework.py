Grades=[] #empty array bucket to put grades into
num=int(input('how many? ')) #get amount of grades from user input
for i in range(0,num,1): #counter to add 'grade' input to 'Grades' array bucket. 
                         #'i' steps through each item in the list, and the range amount is the 'num' input 
    grade=float(input('what is? ')) #get user input for the actual grades
    Grades.append (grade) #adds user input of 'grade' to the 'Grades' array bucket. Remember, 
                          #the amount of times user inputs, is the 'num' amount.
for i in range(0,num,1): #counter for grade equations to get average. 
                         #each grade input by user is added to the sum of the last input,
                         #and then divided by the 'num' of grades.
    gradesToAdd=0 #ALL SWITCH CASES NEED A TEMPORARY VARIABLE.
    gradesToAdd=gradesToAdd+Grades[i] #equation to get grade average. Mind the bracket 
Average=gradesToAdd/num
print(Average)

#To remember order of things maybe try writing pseudo code of what I need to do.
# if there is more than one thing or list, it probably is an array.
# if you are  
