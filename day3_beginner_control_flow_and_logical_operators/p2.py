print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if size == "S":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      output = 15+2+1
      print(f"Your final bill is: ${output}.")
    elif extra_cheese == "N":
      output = 15+2
      print(f"Your final bill is: ${output}.")
  elif add_pepperoni == "N":
    if extra_cheese == "Y":
      output = 15+1
      print(f"Your final bill is: ${output}.")
    elif extra_cheese == "N":
      output = 15
      print(f"Your final bill is: ${output}.")
elif size == "M":
    if add_pepperoni == "Y":
      if extra_cheese == "Y":
        output = 20+3+1
        print(f"Your final bill is: ${output}.")
      elif extra_cheese == "N":
        output = 20+3
        print(f"Your final bill is: ${output}.")
    elif add_pepperoni == "N":
      if extra_cheese == "Y":
        output = 20+1
        print(f"Your final bill is: ${output}.")
      elif extra_cheese == "N":
        output = 20
        print(f"Your final bill is: ${output}.")
elif size == "L":
    if add_pepperoni == "Y":
      if extra_cheese == "Y":
        output = 25+3+1
        print(f"Your final bill is: ${output}.")
      elif extra_cheese == "N":
        output = 25+3
        print(f"Your final bill is: ${output}.")
    elif add_pepperoni == "N":
      if extra_cheese == "Y":
        output = 25+1
        print(f"Your final bill is: ${output}.")
      elif extra_cheese == "N":
        output = 25
        print(f"Your final bill is: ${output}.")
        
        
        
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
