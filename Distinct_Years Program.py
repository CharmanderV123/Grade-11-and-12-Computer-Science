start_year = int(input(""))
checker = True

while(True):
    start_year+=1
    start_year_string = str(start_year)
    counter2 = 0
    while(counter2 <= 4):
        counter = counter2+1
        while(counter < 4):
            if(start_year_string[counter2:counter2+1] != start_year_string[counter:counter+1]):
                checker = True
            elif(start_year_string[counter2:counter2+1] == start_year_string[counter:counter+1]):
                checker = False
                break
            counter+=1
        counter2+=1
        if(checker == False):
            break
    if(checker == True):
        break
print(start_year)
