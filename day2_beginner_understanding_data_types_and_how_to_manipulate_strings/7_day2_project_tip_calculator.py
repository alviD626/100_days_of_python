print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

# N.B. tips are in percentages 
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tips_value = (tip/100) * bill
total_bill = bill + tips_value 
bill_per_person = round(total_bill / people,2)
print(f"Each person should pay: ${bill_per_person}")