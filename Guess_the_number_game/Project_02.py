import random
random_no = random.randint(1,100)
userguess = None
guesses = 0

while (random_no != userguess):
    userguess = int(input("Gues a number from 1 to 100\n"))
    guesses = guesses + 1
    if random_no == userguess:
        print(f'You ave guesed the correct number in {guesses} attempts')
    elif random_no > userguess:
        print(f'You have guesed a smaller number please enter a larger number')
    else:
        print("You have guesed a larger number enter a smaller number")


with open("highscore.txt", "r") as f:
    score = int(f.read())

if guesses<score:
    with open("highscore.txt", "w") as f:
        score = str(f.write(guesses))

     

            