#College_Calculator Application
#26 Sep 2020

print("Tuition")
print("(Please Do Not put Commas)")
tuition_fees = float(input("What is this years tuition fees for the college program you have chosen: $"))
print("Other Annual Costs")
books_and_supplies_fees = float(input("What is the Cost for Books and Supplies: $"))
transportation_fees = float(input("What is the cost for your Transportation (If already included in Tuition fees or if there are none just put 0): $"))
computer_and_monthly_internet_fees = float(input("What is the cost of Computer and Internet (Monthly): $"))
cell_phone_with_data_plan_fees = float(input("What is the cost for your phone with a data plan (Monthly): $"))
entertainment_fees = float(input("What is the cost fot Entertainment (This includes music and movie streaming costs): $"))
other_fees = float(input("Other costs such as clothing: $"))
print("Housing Costs for Students not Living at Home")
print ("(if you live at your own house type zero for every cost)")
residence_with_meal_plan_fees = float(input("Cost of you Residence with a meal plan: $"))
off_campus_housing_fees = float(input("Cost of Off Campus Housing: $"))
food_fees = float(input("Food Costs: $"))
total_cost_without_offset_fees = tuition_fees+books_and_supplies_fees+transportation_fees+(12*computer_and_monthly_internet_fees)+(12*cell_phone_with_data_plan_fees)+entertainment_fees+other_fees
print("Total One-Year Cost without Offset fees: $",total_cost_without_offset_fees)
print("Total cost for Four-Years without offset fees: $",(4*total_cost_without_offset_fees))
print("Offset Costs")
education_savings_plan = float(input("Education Savings Plan: $"))
additional_parental_money = float(input("Additional Parental Money: $"))
student_savings = float(input("Student saving to date: $"))
student_loans_and_grants = float(input("Student Loans and Grants: $"))
bursaries_and_scholarships = float(input("Bursaries and Scholarships: $"))
total_offset_money = education_savings_plan+additional_parental_money+student_savings+student_loans_and_grants+bursaries_and_scholarships
print ("Total Offset Money for One-Year: $",total_offset_money)
additional_savings_required = total_cost_without_offset_fees-total_offset_money
print("Additional Savings Required (One-Year): $",additional_savings_required)
print("Additional Savings Required (Four-Years): $",(4*additional_savings_required))
print("If the Value is negative you have more than enough savings, if the value is 0 you have the exact amount, and if you have positive number that means you need to save up more.")

