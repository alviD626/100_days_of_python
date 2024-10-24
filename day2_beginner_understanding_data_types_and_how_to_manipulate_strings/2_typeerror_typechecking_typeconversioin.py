# type checking

len("Hello")

print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))


# type conversion

print("123"+"456")
print(int("123")+int("456"))
# print(int("abc")+int("456")) # valueError

# error code
# print("Number of letters in your name: " + len(input("Enter your name: ")))


# correct code
# way1
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# way 2
name = input("Enter your name: ")
print(type(name))
length = len(name)
print(type(length))
print("Number of letters in your name: " + str(length))