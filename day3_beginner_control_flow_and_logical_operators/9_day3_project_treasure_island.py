print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")
side = input("You're at a cross road. Where do you want to go?\n    Type \"left\" or \"right\"\n").lower()
if side == "right":
    print("Fall into a hole. Game Over")
elif side == "left":
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake.\n   Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()

    if swim_wait == "wait":
        door = input("You arrive at the island unharmed. There is house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if  door == "red":
            print("It's a room full of fire.\nGame Over")
        elif door == "blue":
            print("You enter a room of beasts.\nGame Over")
        elif  door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over")
    else:
        print("You get attackted by trout. Game Over")