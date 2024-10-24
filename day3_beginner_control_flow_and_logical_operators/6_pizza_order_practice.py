"""
Write a Pizza Delivery Program

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order. work out their final bill. Use the input() function to get a user's preferences and then add up  the total for their order and tell them how much they have to pay.

Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza(Y or N): +$2
Add pepperoni for medium or large pizza(Y or N): +$3
Add extra cheese for any size pizza(Yor N): +$1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


# process 1
# if  size == "S" or size.lower() == 's':
#     price = 15
#     if  pepperoni.lower() == 'y' or pepperoni == "Y":
#         if  extra_cheese.lower() == 'y' or extra_cheese == "Y":
#             print(f"Your final bill is: ${price + 1 + 2}")
#         else:
#             print(f"Your final bill is: ${price + 2}")
#     print(price)
# elif size == "M" or  size.lower() == 'm':
#     price = 20
#     if pepperoni.lower() == 'y' or pepperoni == "Y":
#         if extra_cheese.lower() == 'y' or extra_cheese == "Y":
#             print(f"Your final bill is: ${price + 1 + 3}")
#         else:
#             print(f"Your final bill is: ${price + 3}")
# else:
#     price = 25
#     if  pepperoni.lower() == 'y' or pepperoni == "Y":
#         if extra_cheese.lower() == 'y' or extra_cheese == "Y":
#             print(f"Your final bill is: ${price + 1 + 3}")
#         else:
#             print(f"Your final bill is: ${price + 3}")


# process 2

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
    
# todo: work out how much to add to their bill based on their pepperoni choise.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill  += 3
        
# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")