import math

def circle(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference

a,c=circle(3)

print("Area:",a , "circumference: ",c)