import random

def game(chance, computer):
    if chance == computer:
        return None
    elif computer == 's' and chance == 'g':
        return False
    elif computer == 's' and chance == 'w':
        return True
    elif computer == 'w' and chance == 'g':
        return False
    elif computer == 'w' and chance == 's':
        return True
    elif computer == 'g' and chance == 's':
        return False
    elif computer == 'g' and chance == 'w':
        return True

computer = print("Comp turn: please select from snake(s), water(w), and gun(g)")
random_No = random.randint (1,3)
if random_No == 1:
    computer = 's'
elif random_No == 2:
    computer = 'w'
elif random_No == 3:
    computer = 'g'

chance = input("your turn: please select from snake(s), water(w), and gun(g)")

print(f"You choose {chance}")
print(f"You choose {computer}")

a = game(chance, computer)
if a == None:
    print("the game is tie")
elif a == True:
    print("You won the game")
elif a == False:
    print("You lose the game")    


