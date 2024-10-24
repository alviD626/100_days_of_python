# exercise 1
"""Using what you have learnt about the len() function and the input() function Try to print out the number of characters in the user input. Write everything in just 1 line of code"""

print(len(input("What is your name?: ")))
print(len("jack"))
print(len("Angela"))


# exercise 2
"""Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation"""
username = input("What is your name? ")
length = len(username)
print(length)