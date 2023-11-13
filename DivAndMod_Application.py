#DivAndMod Application
#29 Sep 2020

integer_one = int(input("Enter an integer:"))
integer_two = int(input("Enter a second integer:"))
integer_division_one = int(integer_one/integer_two)
integer_division_two = int(integer_two/integer_one)
mod_division_one = int(integer_one%integer_two)
mod_division_two = int(integer_two%integer_one)
print(integer_one,"/",integer_two,"=",integer_division_one)
print(integer_one,"%",integer_two,"=",mod_division_one)
print(integer_two,"/",integer_one,"=",integer_division_two)
print(integer_two,"%",integer_one,"=",mod_division_two)
