#Eggs Application
#30 Sep 2020

number_of_eggs_purchased = int(input("Enter the number of eggs purchased:"))
dozens_of_eggs = number_of_eggs_purchased/12
excess_eggs = number_of_eggs_purchased-(dozens_of_eggs*12)
if (dozens_of_eggs < 4):
    total_cost = (dozens_of_eggs*0.5)+((0.5/12)*excess_eggs)
    print("The bill is equal to: ${0:.2f}".format(total_cost))
elif(4 <= dozens_of_eggs < 6):
    total_cost = (dozens_of_eggs*0.45)+((0.45/12)*excess_eggs)
    print("The bill is equal to: ${0:.2f}".format(total_cost))
elif (6 <= dozens_of_eggs < 11):
    total_cost = (dozens_of_eggs*0.4)+((0.4/12)*excess_eggs)
    print("The bill is equal to: ${0:.2f}".format(total_cost))
else:
    total_cost = (dozens_of_eggs*0.35)+((0.35/12)*excess_eggs)
    print("The bill is equal to: ${0:.2f}".format(total_cost))
