#Discriminant Application
#30 Sep 2020

a_value = int(input("Enter the value for a:"))
b_value = int(input("Enter the value for b:"))
c_value = int(input("Enter the value for c:"))
discriminant_formula = (b_value**2)-(4*a_value*c_value)
if (discriminant_formula == 0):
    print("One Root")
elif (discriminant_formula > 0):
    print("Two Roots")
else:
    print("No Root")
