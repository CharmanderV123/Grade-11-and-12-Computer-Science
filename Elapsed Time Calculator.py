#Elapsed_Time_Calculator
#20 Oct 2020

import math

starting_time = int(input("Enter the starting hour:"))
am_or_pm = str(input("Enter am or pm:"))
elapsed_hours = int(input("Enter the number of elapsed hours:"))

if (am_or_pm == "pm"):
    starting_time = starting_time + 12 + elapsed_hours

elif(am_or_pm == "am"):
    starting_time = starting_time + elapsed_hours

else:
    print("Error in Entering am or pm")

if(starting_time%12 == 0):
    time_subtractor = int(starting_time/12)-1

elif(starting_time%12 != 0):
    time_subtractor = math.trunc(starting_time/12)

elapsed_time = starting_time - (time_subtractor*12)

if(time_subtractor/2 == 0):
    print(str(elapsed_time)+":00 pm")

else:
    print(str(elapsed_time)+":00 am")
    
