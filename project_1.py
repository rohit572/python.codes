import random 

rock = '''
    _______
---'   ____)__
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)______
            ______)
            _______)
            _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)______
            ______)
        __________)
        (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("what do you  choose? Type 0 for Rock, 1 for Paper, 2 for scissors.\n"))

if user_choice >= 3 and user_choice <= 0: 
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer choice")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Wins!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("you Win!")
    elif computer_choice == user_choice:
        print("It's a draw!")