# print("Welcome to the tip calculator!")
# total_bill = float(input("What was the total bill? $"))
# tips_percentage = int(input("How much tip wourld you like to give? 10, 12 or 15? "))

# total_person = int(input("How many people to split the bill? "))

# if tips_percentage == 10:
#     total_price = (tips_percentage/100)*total_bill
#     final_bill = total_bill+total_price
#     print(f"Each person should pay: ${final_bill/total_person:.2f}")
# elif tips_percentage == 12:
#     total_price = (tips_percentage/100)*total_bill
#     final_bill = total_bill+total_price
#     print(f"Each person should pay: ${final_bill/total_person:.2f}")
# elif tips_percentage == 15:
#     total_price = (tips_percentage/100)*total_bill
#     final_bill = total_bill+total_price
#     print(f"Each person should pay: ${final_bill/total_person:.2f}")


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")