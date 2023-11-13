#Epidemiology Application
#2 Oct 2020

value_p = int(input("Enter the value of p (p<=10 power of 7):")) 
value_n = int(input("Enter the the number of people who have diease on day 0(n<=p):"))
value_r = int(input("Enter the exact number of people they infect on the next day(r<=10):"))
counter = 1
if (value_p > 10**7 or value_n > value_p or value_r > 10):
    print("Error in Input")
else:
    while(value_n <= value_p+1):
        counter = counter + 1
        value_n = value_n+(value_n**value_r)
    print(counter)

