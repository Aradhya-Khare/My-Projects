print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
select = input('Chosse which way you want to turn "left" of "right": \n').lower()
if select == "left":
    select1 = input('If you want to swim select "swim" or if you want to walk from the door select "walk": \n').lower()
    if select1 == "walk":
        select2 = input('There are three doors of different colours they are "blue", "red", and "yellow" select any one colour: \n').lower()
        if select2 == "blue":
            print("Congratulations!, You found the treasure, You win")
        elif select2 == "red" or select2 == "yellow":
            print("Sorry wrong path, Game over")
        else:
            print("Invalid input")

    elif select1 == "swim":
        print("Crocodiles in the lake, Game over")
    else:
        print("Invalid input")

elif select == "right":
    print("You fell into he valley, Game over")
else:
    print("Invalid input")