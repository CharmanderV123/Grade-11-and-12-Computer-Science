#Big_Bang_Secrets_Program
#11 November 2022

# This program receives the user's response which is the message to be decoded using the parameters give to us by the question

shift_value = int(input("Enter K Value:"))                                          #This Variable receives the respnse from user and stores the number of shifts the user had their message encoded in
string = str(input("Enter a String:")).upper()                                      #This Variable stores the message to be decoded in uppercase
decoded_string = ""                                                                 #This is the Variable which will store the decoded message as a string
counter = 1                                                                         #This Variable is initialized with the value one which is incremented later in the program
for character in string:                                                            #This for loop executes the code again and again until it has executed it length of "string" variable times
    unicode_value = ord(character)                                                  #This variable stores the unicode value of each character in the string "string"
    if (65 <= unicode_value <= 90):                                                 #This If statement checks if the unicaode value of the character is within the range of the uppercase letters A-Z if not the program will go to the print error statement portion of the program
        unicode_value-= (3*counter+shift_value)                                     #The Variable containing the unicode value of the character is modified to find the characters decoded value
        if(65 <= unicode_value <= 90):                                              #This if statement checks if the unicode value of the character is within the range of the unicode values of uppercase A-Z
            decoded_string = decoded_string + chr(unicode_value)                    #If the statement above is true then the character is added to the decoded string
        elif(unicode_value > 90):                                                   #Checks to see if the value if greater thatn the max unicode value between Upper A-Z if true executes the code within it
            decoded_string = decoded_string + chr((unicode_value-90)-64)            #Adds the decoded character after modifying its unicode value so it falls in range of the Upper A-Z unicode values
        elif(unicode_value < 65 and unicode_value > 0):                             #Checks to see if the unicode value is less than the unicode values between upper A-Z then executes the code under it
            decoded_string = decoded_string + chr(unicode_value+26)            #Adds the decoded character after modifying its unicode value so its falls in range of upper A-Z unicode values
    else:                                                                           #If all the previous if statements are not executed then the code goes to this else statement
        print("An Error Occured While Computing:")                                  #Prints that a non alphabetic character has been inputted
    counter+=1                                                                      #The counter variable is incremented by 1
print(decoded_string)                                                               #The decoded message is printed

