#Alien_Program
#6 Oct 2020

#This program will identify which type of alien the witness saw by asking the user for number of antennas and eyes the alien which the witness saw had

number_of_antennas = int(input("How many antennas? "))                  #Asks user for the number of antennas the alien had

print()                                                                 #Gives a blank space

number_of_eyes = int(input("How many eyes? "))                          #Asks user fot the number of eyes the alien had

print()                                                                 #Gives a blank space

if(number_of_antennas <= 2 and number_of_eyes <= 3):                    #Checks to see if the alien had the number of eyes and antennas of a GraemeMercurian alien
    alien_type_1 =("GraemeMercurian")                                   #Gives the alien type 1 variable a string value
    print(alien_type_1)                                                 #Outputs the value of alien type 1 (Which has the name of what type of alien the witness had seen)

else:                   
    alien_type_1 =("")                                                  #This line sets the value of alien type 1 to a string containing nothing which will be used in future program

if(number_of_antennas <= 6 and number_of_eyes >=2):                     #Checks to see if the alien had the number of eyes and antennas of a VladSaturnian alien
    alien_type_2 =("VladSaturnian")                                     #Gives the alien type 2 variable a string value (The name of alien)
    print(alien_type_2)                                                 #Outputs the value of alien type 2 (Which has the name of what type of alien the witness had seen)

else:
    alien_type_2 =("")                                                  #Gives the alien type 2 variable a string value of nothing

if(number_of_antennas >= 3 and number_of_eyes <=4):                     #Checks to see if the alien had the number of eyes and antennas of a TroyMartian alien
    alien_type_3 =("TroyMartian")                                       #Gives the alien type 3 variable a string value (The name of alien)
    print(alien_type_3)                                                 #Outputs the value of alien type 3 (Which has the name of what type of alien the witness had seen)

else:
    alien_type_3 =("")                                                  #Gives the alien type 3 variable a string value of nothing

if(alien_type_1 =="" and alien_type_2 =="" and alien_type_3 ==""):      #Checks to see if alien type 1,2, or 3 have a value if they don't then the alien seen by witness isn't any of the three known ones
    print("No Match Found")                                             #Outputs "No Match Found" showing that the alien seen by the witness isn't one we know yet
