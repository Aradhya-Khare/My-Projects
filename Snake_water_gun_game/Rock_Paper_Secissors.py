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

#Write your code below this line 👇

list = [rock, paper, scissors]
Your_chance = int(input('Please choose "0" for slelcting Rock, "1" for selecting Paper or "2" for selecting Secissors\n'))
if Your_chance > 2 or Your_chance < 0:
    print("Invalid input")
else:
    print(list[Your_chance])


computer_chance = random.randint(0,2)
print("Computer chosses")
print(list[computer_chance])


if Your_chance == computer_chance:
    print("Its a draw")
elif Your_chance == 0 and computer_chance == 2:
    print("You win") 
elif Your_chance == 0 and computer_chance == 1:
    print("You loose") 
elif Your_chance == 1 and computer_chance == 0:
    print("You win")
elif Your_chance == 1 and computer_chance == 2:
    print("You loose")
elif Your_chance == 2 and computer_chance == 1:
    print("You win")  
elif Your_chance == 2 and computer_chance == 0:
    print("You loose")
