import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")


if computer_choice == 0  and user_choice == 2:
    print("You lose!")
elif computer_choice == 1 and user_choice == 0:
    print("You lose!")
elif computer_choice == 2 and user_choice == 1:
    print("You lose!")
elif computer_choice == 2  and user_choice == 0:
    print("You Win!")
elif computer_choice == 0 and user_choice == 1:
    print("You Win!")
elif computer_choice == 1 and user_choice == 2:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You typed an invalid number, you lose!")