"""
Question 1:
Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))

1. 10
2. 12.0
3. 0.21
4. 14

Ans: 2. 12.0

"""


"""
Question 2:
What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

1. Syntax Error
2. 15
3. 10
4. (5,10)

Ans: 2. 15

"""


"""
Question 3:
What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

1. NameError
2. SyntaxError
3. None
4. "Pass"
5. "Great"


Ans: 3. None


"""