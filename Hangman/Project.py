import random
list_of_words  = ["apple", "bananna", "watermelons", "strawberry", "grapes", "chikoo"]
word = random.choice(list_of_words)
lives = 6

lst = []
for i in range (len(word)):
    lst += "_"

Game_over = False

while not Game_over: 
    guess = input("Enter a letter: ").lower()
    for n in range (len(word)):
        letter = word[n]
        if letter == guess:
            lst[n] = letter
    
    if guess in lst:
        print(f"You already have guesed the letter {guess}")


    if guess not in word:
        print("You guesed wrong letter, better luck nxt time")
        lives -= 1
        if lives == 0:
            Game_over = True
            print("You lost")

    print(lst)

    if "_" not in lst:
        Game_over = True
        print("You win.")





