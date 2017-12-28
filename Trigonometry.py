import math

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init
def GetAngleOfLineBetweenTwoPoints(p1, p2):
    xDiff = p2.x - p1.x
    yDiff = p2.y - p1.y
    return math.degrees(math.atan2(yDiff, xDiff))
p1 = Point(1,1)
p2 = Point(5,5)

angle1 = GetAngleOfLineBetweenTwoPoints(p1,p2)
#distance = 10 / Cos(angle1)
#newpointy = distance * Sin(angle1)

newpointy = 10 * math.tan(math.radians(angle1)) 

p3 = Point(10, newpointy)

angle2= GetAngleOfLineBetweenTwoPoints(p2, p3)

print(newpointy)
print(angle1,angle2)
