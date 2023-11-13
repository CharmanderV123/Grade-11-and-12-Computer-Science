#EquivalentFractions Application
#1 Oct 2020

import random
print("Equivalent Fractions Quiz")
print("1. 21/3")
print("2. 2/3")
print("3. 4/3")
print("4. 28/4")
print("5. 8/12")
print("6. 1 1/3")
print("7. 5/1")
print("8. 125/5")
counter=0
while (counter < 8):
    question = random.randint(1,8)
    if (question == 1):
        answer = int(input("Which fraction number is equivalent to fraction #1? #"))
        if (answer == 4):
            print("Correct")
        else:
            print("Incorrect the correct answer is #4")
    elif (question == 2):
        answer = int(input("Which fraction number is equivalent to fraction #2? #"))
        if (answer == 5):
            print("Correct")
        else:
            print("Incorrect the correct answer is #5")
    elif (question == 3):
        answer = int(input("Which fraction number is equivalent to fraction #3? #"))
        if (answer == 6):
            print("Correct")
        else:
            print("Incorrect the correct answer is #6")
    elif (question == 4):
        answer = int(input("Which fraction number is equivalent to fraction #4? #"))
        if (answer == 1):
            print("Correct")
        else:
            print("Incorrect the correct answer is #1")
    elif (question == 5):
        answer = int(input("Which fraction number is equivalent to fraction #5? #"))
        if (answer == 2):
            print("Correct")
        else:
            print("Incorrect the correct answer is #2")
    elif (question == 6):
        answer = int(input("Which fraction number is equivalent to fraction #6? #"))
        if (answer == 3):
            print("Correct")
        else:
            print("Incorrect the correct answer is #3")
    elif (question == 7):
        answer = int(input("Which fraction number is equivalent to fraction #7? #"))
        if (answer == 8):
            print("Correct")
        else:
            print("Incorrect the correct answer is #8")
    elif (question == 8):
        answer = int(input("Which fraction number is equivalent to fraction #8? #"))
        if (answer == 7):
            print("Correct")
        else:
            print("Incorrect the correct answer is #7")
    counter = counter +1
