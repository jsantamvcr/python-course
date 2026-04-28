# game rock paper sicciors
import random

# create a list of options
options = ["rock", "paper", "scissors"]
# get user input
user_choice = input("Enter your choice (rock = 1, paper = 2, scissors = 3): ")

# convert user input to an integer
try:
    user_choice = int(user_choice)
except ValueError:
    print("Invalid input. Please enter a number between 1 and 3.")
    exit()  
    
if user_choice < 1 or user_choice > 3:
    print("Invalid input. Please enter a number between 1 and 3.")
    exit()
    
# get computer choice
computer_choice = random.randint(1, 3)
# determine the winner
if user_choice == computer_choice:
    print("It's a tie!") #Tie in spanish is "Empate"
elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
    print("You win!")
else:    print("Computer wins!")

