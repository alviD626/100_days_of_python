programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from runnig as expected.",
    "Function" : "A piece of code that you can easily call over again."
}
print("\n")
print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}

programming_dictionary["Bug"] = "A moth in your computer."
print("\n")
print(programming_dictionary)
print("\n")

for key in programming_dictionary:
    print(key)
    print("\n")
    print(programming_dictionary[key])