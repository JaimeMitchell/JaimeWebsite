class Rectangle: #Class
    def __init__(self,c,l,w): #Self means telling initialization method what name is: myRect1,myRect2... and after Self, other perameters of the rectangles
        self.color=c
        self.length=l
        self.width=w
    def area(self):  # Methods must all have 'self' as it's 1ST PERIMETER
        self.A=self.length*self.width  # Perimeters START WITH 'self.'
        return self.A  # Return value
    def per(self):
        self.perimeter=2*self.length+2*self.width
        return self.perimeter
    def diag(self):
        self.diagonal=(self.width**2+self.length**2)**(1/2)
        return self.diagonal
    def vol(self,h): #passing 'h' to add height variable in the method
        self.height=h
        self.volume=self.length*self.width*self.height
        return self.volume
myRect1=Rectangle('red',2,1)  #Objects name is initalized(=) to their CLASS
myRect2=Rectangle('blue',4,3)

print('Color is: ',myRect1.color)
print('Length is: ',myRect1.length)
print('Width is: ',myRect1.width)
print('Area is: ',myRect1.area())
print('Perimeter is: ',myRect1.per())
print('Diagonal is: ',myRect1.diag())
myVol=myRect1.vol(5)
print('Volume is: ',myVol)
print('Height is: ',myRect1.height)
print('')
print('Color is: ',myRect2.color)
print('Length is: ',myRect2.length)
print('Width is: ',myRect2.width)
print('Area is: ',myRect2.area())
print('Perimeter is: ',myRect2.per())
print('Diagonal is: ',myRect2.diag())
myVol=myRect2.vol(5)
print('Volume is: ',myVol)
print('Height is: ',myRect2.height)
print(2.236*2.236)
