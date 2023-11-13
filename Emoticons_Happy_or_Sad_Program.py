#Emoticons_Happy_or_Sad_Program
#23 Oct 2020

# This code will use the string provided by user and check to see if the user is happy or sad if it is unable to determine the feeling of user the program will display none

input_string = str(input(""))                   # This line gets the input string from the user or phrase you can say
happy_emoticons = input_string.count(":-)")     # This line assigns the happy_emoticons variable with the value of how many :-) are contained in the phrase/string given by user
sad_emoticons = input_string.count(":-(")       # This line assigns the sad_emoticons variable with the value of how many :-( are contained in the phrase/string given by user
if(happy_emoticons < sad_emoticons):            # This line checks whether there are more sad emoticons contained in the phrase/string or happy emoticons contained in the phrase/string
    print("sad")                                # This line prints/outputs sad if the if statement is true
elif(happy_emoticons > sad_emoticons):          # This line checks whether there are more happy emoticons contained in the phrase/string or sad emoticons contained in the phrase/string
    print("happy")                              # This line prints/outputs happy if the elif statement is true
else:                                           # If none of the if and elif statements above are true then the code will do the else statement
    print("none")                               # This line prints/outputs none if the happy_emoticons and sad_emoticons are equal 
