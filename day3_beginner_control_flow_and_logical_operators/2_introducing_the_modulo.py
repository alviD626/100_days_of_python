# exercise 1
"""
what is 10 % 3

What do you think this will output?
"""
print(10 % 3)


# exercise 2
""""
check Odd or Even

write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even". 

"""
number_to_check = int(input("What is the number you want to check?"))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")