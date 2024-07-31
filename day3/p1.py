print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
print("\tType \"left\" or \"right\"")

right_left = input()

if right_left == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("\tType \"wait\" to wait for a boat. Type \"swim to swim across.")
    wait_swim = input()
    
    if wait_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("\tOne red, one yellow and one blue. Which colour do you choose?")
        red_yellow_blue = input()
        if red_yellow_blue == "red":
            print("It's a room full of fire. Game Over.")
        elif red_yellow_blue == "yellow":
            print("You found the treasure! You Win!")
        elif red_yellow_blue == "blue":
            print("You enter a room of beasts. Game Over.")
            
    elif wait_swim == "swim":
        print("You get attacked by an angry trout. Game Over.")
        
elif right_left == "right":
    print("You fell into a hole. Game Over.")