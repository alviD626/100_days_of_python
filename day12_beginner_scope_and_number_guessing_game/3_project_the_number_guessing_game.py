import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,101)
print(random_number)
if choose_level.lower() == "easy":
    i = 10
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        choose_number = int(input("Make a guess: "))
        if  choose_number == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        elif choose_number != random_number:
            if choose_number < random_number:
                print("Too low")
                print("Guess agin")
            elif  choose_number > random_number:
                print("Too high")
                print("Guess agin")
        i -= 1

        
        
elif choose_level.lower() == "hard":
    i = 5
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        choose_number = int(input("Make a guess: "))
        if  choose_number == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        elif choose_number != random_number:
            if choose_number < random_number:
                print("Too low")
                print("Guess agin")
            elif  choose_number > random_number:
                print("Too high")
                print("Guess agin")
        i -= 1