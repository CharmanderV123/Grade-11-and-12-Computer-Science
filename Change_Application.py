#Change Application
#29 Sep 2020

change_in_cents = int(input("Enter the change in cents:"))
quarters = int(change_in_cents/25)
dimes = int((change_in_cents-(quarters*25))/10)
nickels = int((change_in_cents-((quarters*25)+(dimes*10)))/5)
pennies = int((change_in_cents-((quarters*25)+(dimes*10)+(nickels*5))))
print("The Minimum Number of Coins is:")
print("Quarters:",quarters)
print("dimes:",dimes)
print("nickels:",nickels)
print("pennies:",pennies)
