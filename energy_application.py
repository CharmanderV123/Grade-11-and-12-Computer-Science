#Energy Application
#28 Sep 2020

mass = float(input("Enter the mass in kilograms:"))
speed = (3.0*(10**8))
energy = int(mass*speed**2)
light_bulbs_lit = int(energy/360000)

print("The energy produced in Joules is =","{0:.2e}".format(energy))
print("The number of 100-watt light bulbs powered =",str("{0:.2e}".format(light_bulbs_lit)))
