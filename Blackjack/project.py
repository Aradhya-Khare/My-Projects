import random

def The_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def Calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(Your_scores, Comp_scores):
    if Your_scores > 21 and Comp_scores > 21:
        return "You went over You loose"
    if Your_scores == Comp_scores:
        return "Draw"
    elif Your_scores == 0:
        return "You win with a blackjack"
    elif Comp_scores == 0:
        return "You loose because opponent has blackjack"
    elif Your_scores > 21:
        return "You loose as your score exceds 21"
    elif Comp_scores > 21:
        return "You win and Opponent looses as his score exceeds 21"
    elif Your_scores > Comp_scores:
        return "You win as your score is greater than your opponent"
    elif Comp_scores > Your_scores:
        return "You looses as your score is less than your opponent"
    else:
        return "Invalid input"
def game():
    Your_cards = []
    Comp_cards = []
 


    for i in range(2):
        Your_cards.append(The_card())
        Comp_cards.append(The_card())   
        
    game_over = False

    while not game_over:
        Your_score = Calculate_score(Your_cards)
        Comp_score = Calculate_score(Comp_cards)

        print(f"Opponent selected {Comp_cards[0]}")
        print(f"You cards are {Your_cards} and your score is {Your_score}")

        if Your_score > 21 or Comp_score == 0 or Your_score == 0:
            game_over = True
        else:
            a = input("Please enter 'y' if you want to continue the game or enter 'n' if you want to stop the game").lower()
            if a == 'y':
                Your_cards.append(The_card())
            elif a == 'n':
                game_over = True
            else:
                print("Invalid input")
                game_over = True

    while Comp_score != 0 and Comp_score < 17:
        Comp_cards.append(The_card())

    print(f"Your final cards are {Your_cards} and your final score is {Your_score}")
    print(f"Opponent's final cards are {Comp_cards} and Opponent's final score is {Comp_score}")
    print(compare(Your_score, Comp_score))

game()



