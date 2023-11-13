#DogTreats Application
#2 Oct 2020

small_treats = int(input("Enter the number of small treats Barley ate:"))
medium_treats = int(input("Enter the number of medium treats Barley ate:"))
large_treats = int(input("Enter the number of large treats Barley ate:"))
scores = (3*large_treats)+(2*medium_treats)+(small_treats)

if (scores >= 10):
    print("Happy")
else:
    print("Sad")
