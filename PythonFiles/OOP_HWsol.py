class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    
    def gInput(self,ng):
        self.ng=ng
        self.grades=[]
        for i in range(0,self.ng,1):
            prompt='Please enter '+self.first+"'s Grade: "
            grd=float(input(prompt))
            self.grades.append(grd)
        return self.grades
    
    def avGrade(self):
        bucket=0
        for i in range(0,self.ng,1):
            bucket=bucket+self.grades[i]
        avg=bucket/self.ng
        return avg

    def highLow(self):
        highGrade=0
        lowGrade=100
        for i in range(0,self.ng,1):
            if self.grades[i]>highGrade:
                highGrade=self.grades[i]
            if self.grades[i]<lowGrade:
                lowGrade=self.grades[i]
        return lowGrade,highGrade
        
    def printGrades(self):
        for i in range(0,self.ng-1,1): # needs to be one less in order to not go beyond the range of 'number'. 1st loop is the first switch condition that occurs, but it would stop there if not for the next for loop.
            for i in range(0,self.ng-1,1): # Nested for loop ensures the switching occurs with all numbers, not just the first time the condition is true/false.
                if self.grades[i]<self.grades[i+1]: # If 'Current i' is less than the 'Next i' in the array
                    swap=self.grades[i] # set temporary variable In order to avoid breaking switch (first low number will replace ever one it's compared to.
                              # Placement of the variable after conditional statement, and before switch, is important because if I initialize before the switch breaks in the same way as above (no swap variable).
                    self.grades[i]=self.grades[i+1] #the current i equals the i that comes after it and,
                    self.grades[i+1]=swap # The i that comes after the current i becomes the current i, swapping position by swapping identities.
        print(self.first,self.last,"'s Grades are: ")
        for i in range(0,self.ng,1):
            print(self.grades[i])
        print('')

student1=Students('Jaime','Mitchell')
student1.gInput(4)
student2=Students('Shirly','Mclain')
student2.gInput(4)
print('')
print('Grade Report for ',student1.first,student1.last)
print('Average is: ',student1.avGrade())
lowGrade,highGrade=student1.highLow()
print('Low Grade is: ',lowGrade)
print('High Grade is: ',highGrade)
student1.printGrades()
print('')
print('Grade Report for ',student2.first,student2.last)
print('Average is: ',student2.avGrade())
lowGrade,highGrade=student2.highLow()
print('Low Grade is: ',lowGrade)
print('High Grade is: ',highGrade)
student2.printGrades()
