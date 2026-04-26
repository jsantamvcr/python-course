# Welcome to Treasure Island.
# Your mission is to find the treasure.

# Step 1: Ask the user "left or right?"
# If "Left" -> Continue to the next step.
# If "Right" or "anything else" -> Print "Fall into a hole. Game Over."

# Step 2: Ask the user "swim or wait?"
# If "Wait" -> Continue to the next step.
# If "Swim" or "anything else" -> Print "Attacked by trout. Game Over."

# Step 3: Ask the user "Which door?" (Red / Blue / Yellow)
# If "Yellow" -> Print "You Win!"
# If "Red" -> Print "Burned by fire. Game Over."
# If "Blue" -> Print "Eaten by beasts. Game Over."
# If "anything else" -> Print "Game Over."

print(r"""                     .---.
                   .'_..._'.
                  .''_   _''.
                 .' :  '  : '.
                .'_.-'_~_'-._'.
               .'(     '     )'.
              .'  \ \     / /  '.
             .'    \ \   / /    '.
       ____________'''` '```____________
      /              .''.               \
     /              (  ` )               \
    /               .'..'.                \
   /                '----'                 \
  /_________________________________________\
    \  /'--'                       '--'\  /
     ||                                 ||
     ||                                 ||
    _||_                               _||_
    '--'                               '--' """)

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n: ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
