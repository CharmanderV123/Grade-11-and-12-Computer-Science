#Analysis
#14 Sept 2021

import statistics
user_input = 1
num_list = []
count_list = []
average = 0
histo = ""

while(True):
    user_input = int(input("Type Numbers Between 1-50 Inclusively and Input 0 To End the List: "))
    if (user_input >= 1 and user_input <= 50):
        num_list.append(user_input)

    elif (user_input == 0):
        break
    
    else:
        print("Some Error Occured")
        break

        
max_value = max(num_list)
min_value = min(num_list)
for index in num_list:
        average = average + index

print("Max Value",max_value)
print("Minimum Value" ,min_value)
print("Average",average/len(num_list))
print("Range", min_value, "to", max_value)

start = 1
stop = 6
for num in range(10):
    count = 0
    for values in range(start,stop):
        count += (num_list.count(values))
    count_list.append(count)
    histo =""
    for values in range (count_list[num]):
        histo += "*"
    
    print("{:2} {:2} {:2} {:2} {:2}".format(start,"-", stop-1, ":", histo))
    start += 5
    stop += 5
