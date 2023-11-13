#Digit Application
#27 Sep 2020

three_digit_number = int(input("Enter a three digit number:"))
hundreds_place_digit = int(three_digit_number/100)
tens_place_digit = int((three_digit_number-(hundreds_place_digit*100))/10)
ones_place_digit = int(three_digit_number-((hundreds_place_digit*100)+(tens_place_digit*10)))
print("The hundreds-place digit is:",hundreds_place_digit)
print("The tens-place digit is:",tens_place_digit)
print("The ones_place digit is:",ones_place_digit)
