from vpython import *
from time import *
mRadius=.75
wallThickness=.1
roomWidth=10
roomHeight=5
roomDepth=10
left=roomWidth/2
right=roomWidth/-2
up=roomHeight/2
down=roomHeight/-2
back=roomDepth/-2

floor = box(pos=vector(0, up, 0),size=vector(roomWidth,wallThickness,roomDepth))
ceiling = box(pos=vector(0, down, 0), size=vector(roomWidth,wallThickness,roomDepth))
right = box(pos=vector(right, 0, 0), size=vector(wallThickness,roomHeight,roomDepth))
left = box(pos=vector(left, 0, 0), size=vector(wallThickness,roomHeight,roomDepth))
back = box(pos=vector(0, 0, back), size=vector(roomWidth,roomHeight,wallThickness))
marble=sphere(radius=mRadius,color=color.red)
deltaX=.1
xPos=0
while True:
    rate(50)
    xPos=xPos+deltaX
    if xPos>roomWidth/2-.75 or xPos<roomWidth/-2+.75:
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)
    
    

