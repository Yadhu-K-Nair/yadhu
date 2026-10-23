import math
radius=float(input("enter the radius: "))
area=math.pi*radius*radius
circumference=2*math.pi*radius
area_integer=int(area)
print(f"Area:{area:2f}")
print(f"Circumference:{circumference:2f}")
print(f"Area as in:{area_integer}")