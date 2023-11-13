#CircleCircumference Application
#30 Sep 2020

radius = int(input("What is the radius of the circle:"))
circumference = 2*radius*3.14
if (radius < 0):
    print("Negative radii are illegal")
else:
    print("The Circumference of the circle is:",circumference)
