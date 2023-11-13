#Appointing_Program
#23 Oct 2020

# This program helps find how many times positions change at the same time in the mathematical city "CS City"

current_year = int(input("Enter the current year:"))                                                    # This variable obtains a value for current_year variable from the user
future_year = int(input("Enter a future year:"))                                                        # This variable obtains a value for future_year variable from the user
year_counter = 0                                                                                        # This variable helps with the math done by the program below and helps break the loop
while(current_year+year_counter <= future_year):                                                        # This loop is used so the program goes through every year it also checks if year_counter variable is less than or equal to the future_year value given by user
    if(year_counter%2 == 0 and year_counter%3 == 0 and year_counter%4 == 0 and year_counter%5 == 0):    # This if statement check if the year_counter is divisible by 2,3,4,5 if this is true then the program goes to next line otherwise it skips this line or whatever is in the if statement body
        print("All Positions change in year",current_year + year_counter)                               # This statement prints/outputs the statement given to it along with the value of current_year + year_counter if the above if statement is true
    year_counter+= 1                                                                                    # This line adds one to the year_counter which helps eventually break the loop and it helps with finding what years all 4 positions are changed
                                                                        
