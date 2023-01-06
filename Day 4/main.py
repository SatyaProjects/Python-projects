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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissor]
user_choice = int(input("Welcome! Type 0 for Rock, 1 for paper and 2 for scissor\n"))
if user_choice >= 3 or user_choice< 0:
    print("You chose an invalid number you lose!")
else:
    print("You chose")
    print(choice[user_choice])
    print("Computer chose")
    computer_choice = random.randint(0, 2)
    print(choice[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
